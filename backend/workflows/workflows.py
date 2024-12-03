import os
from pathlib import Path
import language_tool_python
from transformers import pipeline
from textblob import TextBlob
from langgraph.graph import StateGraph, START, END
import json
import sys
sys.path.append('./')
from agent.agent import Agent
from services.gemini_service import GeminiService


cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_path = Path(parent_dir+"/backend/core/gdbr_Validator.db")
gemini_service = GeminiService()

# Define the workflow state using a custom class
class TextCheckerState:
    def __init__(self, input_text):
        self.input_text = input_text
        self.results = {}
        self.agent_response = None


# Define individual task nodes

# Grammar Check Function
def grammar_check(state: TextCheckerState):
    # Use language_tool_python for grammar and spelling check
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(state.input_text)

    if matches:
        # If there are errors, list them
        errors = [match.message for match in matches]
        state.results["grammar"] = f"Grammar issues found: {', '.join(errors)}"
    else:
        state.results["grammar"] = "No grammar issues detected."

    return state


# Sentiment Analysis Function using Hugging Face's pipeline
def sentiment_analysis(state: TextCheckerState):
    # Use the fine-grained sentiment analysis model (cardiffnlp/twitter-roberta-base-sentiment)
    sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    
    # Analyze the sentiment of the input text
    analysis = sentiment_analyzer(state.input_text)
    
    # Extract the label and score from the analysis result
    label = analysis[0]['label']
    score = analysis[0]['score']

    # Map Hugging Face labels to more user-friendly terms
    if label == "LABEL_0":
        sentiment = "Negative"
    elif label == "LABEL_1":
        sentiment = "Neutral"
    elif label == "LABEL_2":
        sentiment = "Positive"
    else:
        sentiment = "Unknown"
    
    # Add the sentiment result to the state object
    state.results["sentiment"] = f"{sentiment} sentiment detected with confidence {score:.2f}."
    return state

def invoke_service(state: TextCheckerState):
    # Initialize the Agent (ensure you pass the appropriate arguments, such as service and database name)
    agent = Agent(service=gemini_service, db_name=db_path)
    
    # Use the agent to process the user input and provide a GDPR check
    agent_response = agent.invoke_service(state.input_text)
    
    # Store the agent's response in the state object
    state.agent_response = agent_response
    return state

# Create a workflow graph
workflow = StateGraph(TextCheckerState)

# Add nodes to the workflow
workflow.add_node("grammar_check", grammar_check)
workflow.add_node("sentiment_analysis", sentiment_analysis)
workflow.add_node("invoke_service",invoke_service)

# Define edges between nodes
workflow.add_edge(START, "grammar_check")
workflow.add_edge("grammar_check", "sentiment_analysis")
workflow.add_edge("sentiment_analysis","invoke_service")
workflow.add_edge("invoke_service", END)

# Compile the workflow (creating a CompiledStateGraph)
compiled_workflow = workflow.compile()


# Execute the workflow by manually triggering the nodes
if __name__ == "__main__":
    # Ask the user for input text
    user_input = input("Enter a text for grammar and sentiment analysis: ")

    # Initialize the workflow state with the user input
    initial_state = TextCheckerState(input_text=user_input)

    # Process the graph manually
    current_state = initial_state

    # Manually trigger the nodes based on the graph edges
    current_state = grammar_check(current_state)  # "grammar_check"
    current_state = sentiment_analysis(current_state)  # "sentiment_analysis"
    current_state = invoke_service(current_state) # "invoke_service"

    # Print the results after processing
    print("\nWorkflow Results:")
    for key, value in current_state.results.items():
        print(f"{key.capitalize()}: {value}")

    print("\nAgent Response:", current_state.agent_response)    
