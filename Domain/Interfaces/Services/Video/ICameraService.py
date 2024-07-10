from abc import ABCMeta, abstractmethod


class ICameraService(metaclass=ABCMeta):
    @abstractmethod
    def StartStream(self):
        pass
    @abstractmethod
    def ProcessFrame(self, frame, model, recognitionPlateService, vehicles):
        pass
