from pydantic import BaseModel

class VehicleRequestView(BaseModel):
    color: str
    plate: str