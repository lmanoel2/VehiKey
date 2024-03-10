from pydantic import BaseModel

class VehicleView(BaseModel):
    color: str
    plate: str