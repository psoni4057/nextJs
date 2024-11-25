# from agent.agent import Agent
# from services.gemini_service import GeminiService

from fastapi import FastAPI
from backend.agent.agent import Agent
from backend.api.endpoints import compliance
from backend.services.gemini_service import GeminiService



app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}

# gemini_service = GeminiService()
# agent = Agent.agent.Agent(service=gemini_service, db_path='gdbr_Validator.db')
# template = """You are a GDPR expert. Tell if the given data is compliant and the reason.
#                 : {data}. Do not use technical words, give easy-to-understand responses.
#                 The answer should be in JSON format as follows:
#                 compliant: yes/no
#                 reason: """
        
# data = "Today is Monday"  
# result = agent.invoke_service(template, data)
# print(result)