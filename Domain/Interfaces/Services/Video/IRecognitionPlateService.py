from abc import ABCMeta, abstractmethod


class IRecognitionPlateService(metaclass=ABCMeta):
    @abstractmethod
    def GetTextPlateFromImage(self, imageCar) -> str:
        pass

