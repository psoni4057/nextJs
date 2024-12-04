import os
from pathlib import Path
import language_tool_python
from transformers import pipeline
from textblob import TextBlob
from langgraph.graph import StateGraph, START, END
import json
import sys
sys.path.append('./')

from services.gemini_service import GeminiService
from state.datastate import DataState
from agent.agent import invoke_gdpr_agent



# Grammar Check Function
def grammar_check(state: DataState):
    # Use language_tool_python for grammar and spelling check
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(state["input_text"])

    if matches:
        # If there are errors, list them
        errors = [match.message for match in matches]
        state["grammar"] = f"Grammar issues found:"
    else:
        state["grammar"] = "No grammar issues detected."

    return state


# Sentiment Analysis Function using Hugging Face's pipeline
def sentiment_analysis(state: DataState):
    # Use the fine-grained sentiment analysis model (cardiffnlp/twitter-roberta-base-sentiment)
    #sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    
    # Analyze the sentiment of the input text
    #analysis = sentiment_analyzer(state["input_text"])
    
    # Extract the label and score from the analysis result
    #label = analysis[0]['label']
    #score = analysis[0]['score']
    
    # Map Hugging Face labels to more user-friendly terms
    #if label == "LABEL_0":
    #    sentiment = "Negative"
    #elif label == "LABEL_1":
    #    sentiment = "Neutral"
    #elif label == "LABEL_2":
    #    sentiment = "Positive"
    #else:
    #    sentiment = "Unknown"
    
    # Add the sentiment result to the state object
    state["sentiment"] = f" sentiment is not supported."
    return state


   
def initialize_text_workflow():
    workflow = StateGraph(DataState)

    # Add nodes to the workflow
    workflow.add_node("grammar_check", grammar_check)
    workflow.add_node("sentiment_analysis", sentiment_analysis)
    workflow.add_node("invoke_gdpr_agent", invoke_gdpr_agent)

    # Define edges between nodes
    workflow.add_edge(START, "grammar_check")
    workflow.add_edge("grammar_check", "sentiment_analysis")
    workflow.add_edge("sentiment_analysis", "invoke_gdpr_agent")
    workflow.add_edge("invoke_gdpr_agent", END)

    # Compile the workflow (creating a CompiledStateGraph)
    text_workflow = workflow.compile()

    return text_workflow
   

    



   


    
