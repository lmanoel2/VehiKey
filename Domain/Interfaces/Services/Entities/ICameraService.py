from abc import ABCMeta, abstractmethod
from Domain.Entities.Camera import Camera


class ICameraService(metaclass=ABCMeta):
    @abstractmethod
    def Create(self, vehicleView: Camera):
        pass

    @abstractmethod
    def Get(self):
        pass

    @abstractmethod
    def GetById(self, id: int):
        pass

    @abstractmethod
    def Update(self, id: int, model):
        pass