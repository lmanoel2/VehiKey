from pydantic import BaseModel

class VehicleView(BaseModel):
    color: str
    model: str
    plate: str