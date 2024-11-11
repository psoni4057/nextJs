from pydantic import BaseModel, EmailStr
from typing import List, Optional
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
import requests
from typing import Any
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

## Write a Pydantic model that outlines the structure of the data you expect from LLM.
## The model can have the fields like compliant,reason...
class ValidationResponse(BaseModel):
    compliant: str
    reason: str
   
## Define a Parser

parser = PydanticOutputParser(pydantic_object=ValidationResponse)

## Define the prompt template
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

## Write a Service class which will be used to interact with the model
## Interact with gemini use the api call and passing the prompt template
## Return the response as a ValidationResponse object


class GeminiService:
    def __init__(self, api_key: str, model_url: str):
        self.api_key = api_key
        self.model_url = model_url
        self.parser = PydanticOutputParser(pydantic_object=ValidationResponse)

    def generate_response(self, content: str) -> ValidationResponse:
        prompt_input = prompt.format(content=content)
        
        # Calling Gemini API with the formatted prompt
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "gemini-1",                                  
            "messages": [{"role": "system", "content": prompt_input}],
            "temperature": 0.7,
        }

        # Sending API request
        response = requests.post(self.model_url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            # Extracting the response content from the API response
            model_output = result['choices'][0]['message']['content']
            
            # Parse the model's output into the ValidationResponse model
            parsed_response = self.parser.parse(model_output)
            return parsed_response
        else:
            raise Exception(f"Error from Gemini API: {response.text}")