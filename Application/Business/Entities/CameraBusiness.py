import re
from datetime import datetime, timezone

from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Application.Exceptions.Entities.BaseException import ValidTimeNotFormattedError
from Application.Exceptions.Entities.CameraExceptions import IpAlreadyExistsError
from Domain.Entities.Camera import Camera
from Domain.Model.CameraModel import CameraModel


class CameraBusiness(CRUDBusiness):
    def __init__(self):
        super().__init__(Camera)

    def Create(self, model: Camera):
        self.__AlreadyExistIp(model.ip)
        self.__ValidateValidTime(model.valid_time)
        super().Create(model)

    def Update(self, id: int, model: CameraModel):
        camera = self.GetById(id)

        if camera.ip != model.ip:
            self.__AlreadyExistIp(model.ip)

        self.__ValidateValidTime(model.valid_time)
        return super().Update(id, model)

    def GetByIp(self, ip: str) -> Camera:
        return self.Session.query(Camera).filter(Camera.ip == ip).first()

    def GetByController(self, controller: str) -> Camera:
        return self.Session.query(Camera).filter(Camera.controller == controller).first()

    def __AlreadyExistIp(self, ip: str):
        alreadyExistIp = bool(self.GetByIp(ip))

        if alreadyExistIp:
            raise IpAlreadyExistsError()

    def __ValidateValidTime(self, validTime: str):
        if not validTime:
            return

        pattern = r'\d{2}-\d{2}-\d{4}-\d{2}:\d{2} \d{2}-\d{2}-\d{4}-\d{2}:\d{2}'
        patternIsOk = bool(re.match(pattern, validTime))

        if not patternIsOk:
            raise ValidTimeNotFormattedError()

        startDate, endDate = validTime.split()
        datetime.strptime(startDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)
        datetime.strptime(endDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)

