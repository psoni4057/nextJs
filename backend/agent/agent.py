import json
import sqlite3
from urllib import request
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  
from backend.services.gemini_service import GeminiService
from backend.core.config import ConfigRules

class Agent:
    def __init__(self, service, db_name: str):   
        self.service = service
        self.db_name = db_name
        self.conn = None
        self.connect_db()  

    def connect_db(self):
        """Method to connect to SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)  
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            self.conn = None

    def retrieve_rules(self):    
        if self.conn:
            config_rules = ConfigRules(self.db_name)
            config_rules.create_table()
            rules = config_rules.get_all_rules()
            return rules
        else:
            print("Database connection is not established.")
            return []

    def _create_prompt(self, template: str, data: str, rules: str):
        try:
            prompt = template.format(request=data, rules=rules) 
            return prompt
        except KeyError as e:
            print(f"Missing key: {e}")
            return ""
        except Exception as e:
            print(f"Error creating prompt: {e}")
            return ""

    def invoke_service(self, data: str):
        """Create a prompt from the template, invoke the Gemini service, and return the response."""
        all_rules = self.retrieve_rules()
        template = f"""
        You are checking if the user input contains personal data that should be protected under the GDPR.
        A set of rules is provided to you to do the check.
        Only use the rules provided to you.
        Your output should indicate if the input is compliant or non-compliant, and provide a reason for non-compliance.
        
        Here is the user input:
        {data}
        ---
        Here are the rules:
        {json.dumps(all_rules, indent=2)}  # JSON formatted rules for clarity
        """
        prompt_text = self._create_prompt(template, data, json.dumps(all_rules, indent=2))
        
        if prompt_text:
            response_json = self.service.invoke_service(prompt_text)
            if isinstance(response_json, dict):
                response_text = response_json.get('data', '')
            else:
                response_text = response_json
            if not response_text:
                print("No response text received.")
                return {"error": "Empty response text from service"}
            return response_text
        else:
            return {"error": "Error in creating prompt"}
