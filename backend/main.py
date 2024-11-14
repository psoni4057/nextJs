# backend/main.py
from fastapi import FastAPI
from backend.api.endpoints import compliance
import agent.agent


app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}   


agent.agent.invoke_agent()   
