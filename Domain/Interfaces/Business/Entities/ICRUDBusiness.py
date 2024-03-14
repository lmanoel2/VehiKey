from abc import ABCMeta, abstractmethod


class ICRUDBusiness(metaclass=ABCMeta):
    @abstractmethod
    def Create(self, model):
        pass

    @abstractmethod
    def Get(self):
        pass

    @abstractmethod
    def GetById(self, id:int):
        pass

    @abstractmethod
    def Update(self, id: int, model):
        pass

    @abstractmethod
    def Delete(self, model):
        pass

    @abstractmethod
    def DeleteById(self, id: int):
        pass
