import json
import sqlite3
from urllib import request
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  
from services.gemini_service import GeminiService
from core.config import ConfigRules
from state.datastate import DataState

def retrieve_rules():    
    config_rules = ConfigRules()
    rules = config_rules.get_all_rules()
    return rules
        
def create_prompt( template: str, data: str, rules: str):
        try:
            prompt = template.format(request=data, rules=rules) 
            return prompt
        except KeyError as e:
            print(f"Missing key: {e}")
            return ""
        except Exception as e:
            print(f"Error creating prompt: {e}")
            return ""

def invoke_gdpr_agent( state: DataState):
        print("Invoking GDPR agent for input text:", state["input_text"])

        """Create a prompt from the template, invoke the Gemini service, and return the response."""

        all_rules = retrieve_rules()
        prompt_text = True
        print("Prompt text:", prompt_text)
        if prompt_text:
            response_json = GeminiService.invoke_service(state["input_text"],all_rules) 
            if isinstance(response_json, dict):
                response_text = response_json.get('data', '')
            else:
                response_text = response_json
            if not response_text:
                print("No response text received.")
                return {"error": "Empty response text from service"}
            print("Response text:", response_text)
            try:
                response_data = json.loads(response_text)
                response_values = list(response_data.values())
                print("Response values:", response_values)
                statusval= response_values[0]
                if statusval =="Yes,":
                    state["status"] = "Complaint"
                else:
                    state["status"] = "Non Complaint"
                state["results"] = response_values
                state["comments"] = response_values[1]  #Changed
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON response: {e}")
                return {"error": "Invalid JSON response from service"}
            
            return state
        else:
            return {"error": "Error in creating prompt"}
