from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.agents import Tool, create_react_agent

import os
from langchain_core.prompts import BasePromptTemplate
from langchain_core.prompts import PromptTemplate

MODEL_NAME = "gemini-pro"
GOOGLE_API_KEY = "USE_YOUR_GOOGLE_API_KEY"


llm = ChatGoogleGenerativeAI(model=MODEL_NAME,
      google_api_key=GOOGLE_API_KEY,
      convert_system_message_to_human = True,
      verbose = True,
)

