from pydantic import BaseModel
from typing import Optional


class VehicleRequestView(BaseModel):
    color: str
    plate: str
    valid_time: Optional[str] = None
