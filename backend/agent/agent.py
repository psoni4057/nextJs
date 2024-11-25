import json
import sqlite3
from langchain.prompts import PromptTemplate
from backend.services.gemini_service import GeminiService 

class Agent:
    def __init__(self, service: GeminiService, db_path: str):
        self.service = service
        self.db_path = db_path
        self.rules = self._retrieve_rules()

    def _retrieve_rules(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            query = "SELECT rules FROM gdbr_rules" 
            cursor.execute(query)
            rules = cursor.fetchall()
            conn.close()
            return rules
        except Exception as e:
            print(f"Error retrieving rules from database: {e}")
            return {}

    def _create_prompt(self, template: str, data: str):
        try:
            prompt = template.format(data=data) 
            return prompt
        except KeyError as e:
            print(f"Missing key: {e}")
            return ""
        except Exception as e:
            print(f"Error creating prompt: {e}")
            return ""

    def invoke_service(self, template: str, data: str):
        """Create a prompt from the template, invoke the Gemini service, and return the response."""
        prompt_text = self._create_prompt(template, data)
        if prompt_text:  
            response_json = self.service.invoke_service(prompt_text)
            return response_json
        else:
            return "Error in creating prompt"
