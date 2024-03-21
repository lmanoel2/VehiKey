from abc import ABCMeta, abstractmethod


class IGenerateVehicleEventService(metaclass=ABCMeta):

    @abstractmethod
    def SendVehicleOK(self, plate: str):
        pass


    @abstractmethod
    def SendVehicleNotFound(self, plate: str):
        pass

    @abstractmethod
    def SendVehicleOutOfHour(self, plate: str):
        pass
