
from fastapi import FastAPI

from api.endpoints import auditApi, compliance, endpoints
from services.gemini_service import GeminiService
import uvicorn
from core.config import ConfigRules
from core.Audit import Audit
from state.datastate import DataState

## Do all the initializations and start the server 

app = FastAPI()

app.include_router(compliance.router, prefix="/api/v1")
# TO get last 10 auditrecords
app.include_router(auditApi.router, prefix="/api/v1/audit")
# Get all rules
app.include_router(endpoints.router, prefix="/api/v1")
# Adding new Rule
app.include_router(endpoints.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the GDPR Validator API"}



def init_config_rules():
            config_rules = ConfigRules()
            config_rules.create_table()
            return 

def init_audit_records():
    audit_records = Audit()
    audit_records.create_table()
    return

if __name__ == "__main__":

    init_config_rules()
    uvicorn.run(app, host="0.0.0.0", port=8000)

    


