from abc import ABCMeta, abstractmethod


class IPubSubService(metaclass=ABCMeta):

    @abstractmethod
    def Publish(self, message: str):
        pass