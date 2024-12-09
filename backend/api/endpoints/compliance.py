from agent import Auditagent, agent
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
from models.api_data_model import RequestType
from services.check_data_compliance_service import check_compliance

router = APIRouter()

from fastapi import FastAPI
from pydantic import BaseModel

# Define a Pydantic model for the request body
class Item(BaseModel):
    appname: str
    model: str 

app = FastAPI()

@router.post("/compliance/check", response_model=dict)
async def compliance_check(request: RequestType):
    try:
        
        # Delegate to the service layer
        response = check_compliance(request.data, request.dataType, request.dataURL, request.appName, request.model)
    
        return {
            "message": "API run successful",
            "data": response
        }
        

    except HTTPException as e:
        # Return the error raised by the service
        raise e
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

