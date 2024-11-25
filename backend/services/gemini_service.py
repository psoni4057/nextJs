from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr
import json
from langchain.chains import LLMChain  
from typing import List, Optional
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from backend.models.gemini import llm

class ValidationResponse(BaseModel):
    compliant: str
    reason: str
   
# Define a Parser

parser = PydanticOutputParser(pydantic_object=ValidationResponse)

# Write a Service class which will be used to interact with the model
# Interact with gemini use the api call and passing the prompt template
# Return the response as a ValidationResponse object

class GeminiService:
    def invoke_service(self, prompt_text: str):
        prompt_template = PromptTemplate(template="You are a GDPR expert. Tell if the given data is compliant and the reason: {data}.", input_variables=["data"])
        chain = LLMChain(prompt=prompt_template, llm=llm)  # Ensure 'llm' is your language model (e.g., OpenAI, Gemini, etc.)
        response = chain.invoke({"data": prompt_text})
        validated_response = parser.parse(response)
        json_data = json.dumps(validated_response.dict(), indent=4)
        return json_data
