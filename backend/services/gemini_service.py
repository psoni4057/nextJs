from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
import json
from langchain.chains import LLMChain  
from langchain.prompts import PromptTemplate
from models.gemini import llm, llm_openai

from langchain.output_parsers import PydanticOutputParser

class ValidationResponse(BaseModel):
    compliant: str
    reason: str
   
parser = PydanticOutputParser(pydantic_object=ValidationResponse)




class GeminiService:

    @staticmethod
    def invoke_llm_chain(prompt_text,rules: str):
        prompt_template = PromptTemplate(
            template=(
            "You are a GDPR expert. Tell if the given data is compliant as Yes or No "
            "and the reason in a very short sentence. Here is the data: {data}."
            "Use the given rules to override the decision if required."
            "The rules are as follows: {rules}"
            ),
            input_variables=["data","rules"],
        )
        print("Invoking LLM with Prompt template:", prompt_template)
        chain = LLMChain(prompt=prompt_template, llm=llm_openai)
        response = chain.invoke({"data": prompt_text, "rules": rules})
        print("Response from LLM:", response)
        return response
    
    def invoke_service( prompt_text,rules: str):
        
        response = GeminiService.invoke_llm_chain(prompt_text,rules)
        
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
        print("Response JSON:", json_response)
        return json_response
