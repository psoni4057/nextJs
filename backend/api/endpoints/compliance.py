# backend/api/endpoints/compliance.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.models.api_data_model import RequestType
from backend.services.check_data_compliance_service import check_compliance

router = APIRouter()



@router.post("/compliance/check", response_model=dict)
async def compliance_check(request: RequestType):
    try:
        # Delegate to the service layer
        response = check_compliance(request.data, request.dataType, request.dataURL)
        return {
            "message": "Compliance check successful",
            "data": response
        }
    except HTTPException as e:
        # Return the error raised by the service
        raise e
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=str(e))
