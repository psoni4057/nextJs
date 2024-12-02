from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
import json
from langchain.chains import LLMChain  
from langchain.prompts import PromptTemplate
from backend.models.gemini import llm
from langchain.output_parsers import PydanticOutputParser

class ValidationResponse(BaseModel):
    compliant: str
    reason: str
   
parser = PydanticOutputParser(pydantic_object=ValidationResponse)

class GeminiService:
    def invoke_service(self, prompt_text: str):
        prompt_template = PromptTemplate(template="You are a GDPR expert. Tell if the given data is compliant and the reason: {data}.", input_variables=["data"])
        chain = LLMChain(prompt=prompt_template, llm=llm) 
        response = chain.invoke({"data": prompt_text})
        if not response or 'text' not in response:
            print("Error: No valid response received.")
            return {"error": "Empty response text from service"}
        response_text = response['text'].strip()
        try:
            compliant_status, reason = response_text.split(" ", 1)  # Split at first space
        except ValueError:
            print("Error: Response format is invalid")
            return {"error": "Invalid response format"}
        response_dict = {
            "compliant": compliant_status,
            "reason": reason
        }
        json_response = json.dumps(response_dict, indent=4)
        return json_response
