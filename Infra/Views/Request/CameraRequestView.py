from pydantic import BaseModel
from typing import Optional


class CameraRequestView(BaseModel):
    ip: str
    port: int
    password: str
    user: str
    name: str
    manufacturer: str
    valid_time: Optional[str] = None
    controller: Optional[str] = None
