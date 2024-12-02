
from fastapi import FastAPI
from backend.agent.agent import Agent
from backend.api.endpoints import compliance
from backend.services.gemini_service import GeminiService



app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}

#import os
# from pathlib import Path
# from agent.agent import Agent
# from services.gemini_service import GeminiService
# from core.config import ConfigRules

# cwd = os.getcwd()
# parent_dir = os.path.dirname(cwd)
# db_path = Path(parent_dir+"/backend/core/gdbr_Validator.db")
# gemini_service = GeminiService()
# agent = Agent(service=gemini_service, db_name=db_path)
# data = "Password is bhd"  
# result = agent.invoke_service(data)
# print("Result:",result)

