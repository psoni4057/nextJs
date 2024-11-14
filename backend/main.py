# backend/main.py
from fastapi import FastAPI
from backend.api.endpoints import compliance

app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}
import agent.agent

agent.agent.invoke_agent()
