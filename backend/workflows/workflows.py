import language_tool_python
from langgraph.graph import StateGraph, START, END
from textblob import TextBlob

# Define the workflow state using a custom class
class TextCheckerState:
    def __init__(self, input_text):
        self.input_text = input_text
        self.results = {}

# Define individual task nodes
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

def sentiment_analysis(state: TextCheckerState):
    # Real sentiment analysis using TextBlob
    analysis = TextBlob(state.input_text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative"
    state.results["sentiment"] = f"{sentiment} sentiment detected."
    return state

# Create a workflow graph
workflow = StateGraph(TextCheckerState)

# Add nodes to the workflow
workflow.add_node("grammar_check", grammar_check)
workflow.add_node("sentiment_analysis", sentiment_analysis)

# Define edges between nodes
workflow.add_edge(START, "grammar_check")
workflow.add_edge("grammar_check", "sentiment_analysis")
workflow.add_edge("sentiment_analysis", END)

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

    # Print the results after processing
    print("\nWorkflow Results:")
    for key, value in current_state.results.items():
        print(f"{key.capitalize()}: {value}")
