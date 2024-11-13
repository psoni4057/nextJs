from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr
import json
from typing import List, Optional
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from models.gemini import llm

# create the prompt
prompt_template: str = """/
You are a gdpr expert, tell the given data is compliant and the reason / 
: {data}. Do not use technical words, give easy/
to understand responses.
The answer should be in the JSON format as follows:/
compliant: yes/no
reason: 
"""

# Write a Pydantic model that outlines the structure of the data you expect from LLM.
# The model can have the fields like compliant,reason...
class ValidationResponse(BaseModel):
    compliant: str
    reason: str
   
# Define a Parser

parser = PydanticOutputParser(pydantic_object=ValidationResponse)

# Define the prompt template
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["data"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Write a Service class which will be used to interact with the model
# Interact with gemini use the api call and passing the prompt template
# Return the response as a ValidationResponse object

class GeminiService:
    def invoke_service(self,prompt_text):
        self.prompt_text=prompt_text
        chain = prompt | llm
        response = chain.invoke(self.prompt_text)
        validated_response=parser.parse(response.content)
        json_data = json.dumps(validated_response.dict(), indent=4)
        return json_data