from abc import ABCMeta, abstractmethod


class IRecognitionPlateService(metaclass=ABCMeta):
    @abstractmethod
    def GetTextPlateFromImage(self) -> int:
        pass

