from abc import ABCMeta, abstractmethod
from Domain.Entities.Vehicle import Vehicle


class IVehicleService(metaclass=ABCMeta):
    @abstractmethod
    def Create(self, vehicleView: Vehicle):
        pass

    @abstractmethod
    def Get(self):
        pass

    @abstractmethod
    def GetById(self, id:int):
        pass

    @abstractmethod
    def Update(self, id:int, model):
        pass