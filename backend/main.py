
from fastapi import FastAPI

from api.endpoints import compliance
from services.gemini_service import GeminiService
import uvicorn
from core.config import ConfigRules

## Do all the initializations and start the server 

app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}

def init_config_rules():
            config_rules = ConfigRules()
            config_rules.create_table()
            return 

if __name__ == "__main__":
    init_config_rules()
    uvicorn.run(app, host="0.0.0.0", port=8000)


