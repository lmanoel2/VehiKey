from abc import ABCMeta, abstractmethod

from Domain.Entities.Camera import Camera


class ICameraService(metaclass=ABCMeta):
    @abstractmethod
    def StartStream(self, camera: Camera):
        pass
