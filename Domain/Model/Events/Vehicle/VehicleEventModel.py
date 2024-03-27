from datetime import datetime

from pydantic import BaseModel
from Domain.Enumerators.Events.Cmd import Cmd
from Domain.Enumerators.Events.Code import Code


class VehicleOk(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code: int = Code.ACCESS_ALLOWED.value[0]
    plate: str


class VehicleNotFound(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code: int = Code.ACCESS_NOT_FOUND_VEHICLE.value[0]
    plate: str


class VehicleOutOfHour(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code: int = Code.ACCESS_OUT_OF_HOUR.value[0]
    plate: str


class VehicleWithCameraOutOfHour(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code: int = Code.ACCESS_WITH_CAMERA_OUT_OF_HOUR.value[0]
    plate: str
