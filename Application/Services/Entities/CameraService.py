from Application.Business.Entities.CameraBusiness import CameraBusiness
from Domain.Entities.Camera import Camera
from Domain.Interfaces.Services.Entities.ICameraService import ICameraService
from Domain.Model.CameraModel import CameraModel


class CameraService(ICameraService):
    business = CameraBusiness()

    def Create(self, camera: Camera):
        return self.business.Create(camera)

    def Get(self):
        return self.business.Get()

    def GetById(self, id: int):
        return self.business.GetById(id)

    def Update(self, id: int, model: CameraModel):
        return self.business.Update(id, model)

    def DeleteById(self, id: int):
        return self.business.DeleteById(id)
