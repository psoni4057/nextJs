# Request Model
from pydantic import BaseModel


class RequestType(BaseModel):
    data: str
    appName: str
    model: str
    dataURL: str
    dataType: str

# Response Model
class ResponseType(BaseModel):
    message: str
    is_compliant: bool
    appName: str
    status: str