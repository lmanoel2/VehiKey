from Domain.DataBase.Context import Session
from Domain.Interfaces.Business.Entities.ICRUDBusiness import ICRUDBusiness


class CRUDBusiness(ICRUDBusiness):
    Session = Session()
    def Create(self, model):
        raise NotImplementedError()

    def Get(self, id: int):
        raise NotImplementedError()

    def Update(self, model):
        raise NotImplementedError()

    def Delete(self, model):
        raise NotImplementedError()