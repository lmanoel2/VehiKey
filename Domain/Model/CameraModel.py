from pydantic import BaseModel


class CameraModel(BaseModel):
    ip: str
    port: str
    password: int
    user: str
    name = str
    manufacturer = str
    access_time = str