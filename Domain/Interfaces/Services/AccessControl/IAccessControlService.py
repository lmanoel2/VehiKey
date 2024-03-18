from abc import ABCMeta, abstractmethod


class IAccessControlService(metaclass=ABCMeta):
    @abstractmethod
    def ProcessPlate(self, plate: str, plateScore: float):
        pass
