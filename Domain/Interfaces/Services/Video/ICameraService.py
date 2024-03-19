from abc import ABCMeta, abstractmethod


class ICameraService(metaclass=ABCMeta):
    @abstractmethod
    def StartStream(self):
        pass
