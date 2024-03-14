from abc import ABCMeta, abstractmethod


class ICRUDBusiness(metaclass=ABCMeta):
    @abstractmethod
    def Create(self, model):
        pass

    @abstractmethod
    def Get(self):
        pass

    @abstractmethod
    def Update(self, model):
        pass

    @abstractmethod
    def Delete(self, model):
        pass
