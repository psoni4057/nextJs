from pydantic import BaseModel, EmailStr
from typing import List, Optional
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
