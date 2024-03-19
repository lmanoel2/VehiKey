from pydantic import BaseModel
from Domain.Enumerators.Events.Cmd import Cmd
from Domain.Enumerators.Events.Code import Code


class VehicleOk(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    code: int = Code.ACCESS_ALLOWED.value[0]


class VehicleNotFound(BaseModel):
    cmd: str = Cmd.ACCESS_VEHICLE.value
    code: int = Code.ACCESS_NOT_FOUND_VEHICLE.value[0]
