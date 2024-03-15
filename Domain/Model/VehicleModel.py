from pydantic import BaseModel
from typing import Optional


class VehicleModel(BaseModel):
    color: str
    plate: str
    valid_time: Optional[str] = None
    access_time: Optional[str] = None
    number_access: Optional[int] = None
