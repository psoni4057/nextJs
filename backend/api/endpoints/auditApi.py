from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from core.Audit import Audit  


router = APIRouter()
class AuditRecord(BaseModel):
    id: int
    Date: str
    AppName:str
    Model: str
    Compliance_Area: str
    Status: str
    Comments: str

audit = Audit.create_audit()

@router.get("/")
async def fetch_records():
    try:
        records = audit.get_records()
        formatted_records = [
            AuditRecord(
                id=row[0], 
                Date=row[1], 
                AppName=row[2], 
                Model=row[3], 
                Compliance_Area=row[4], 
                Status=row[5], 
                Comments=row[6]
            ) for row in records
        ]
        return {"data": formatted_records}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

