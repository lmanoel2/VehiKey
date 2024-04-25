from abc import ABCMeta, abstractmethod


class ISaveEventService(metaclass=ABCMeta):

    @abstractmethod
    def SaveEvent(self, event: str, serialNumber: str):
        pass
