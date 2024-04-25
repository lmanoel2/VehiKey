from datetime import datetime

from pydantic import BaseModel
from Domain.Enumerators.Events.Cmd import Cmd
from Domain.Enumerators.Events.Code import Code


class DoorStatus(BaseModel):
    cmd: str = Cmd.DOOR_STATUS.value
    date: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code: int = Code.ACCESS_ALLOWED.value[0]
    from_controller: str
    from_camera: int
