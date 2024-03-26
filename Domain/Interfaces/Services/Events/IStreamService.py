from abc import ABCMeta, abstractmethod


class IStreamService(metaclass=ABCMeta):

    @abstractmethod
    def HandleConnect(self):
        pass