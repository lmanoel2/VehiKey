from Domain.DataBase.Context import Session
from Domain.Interfaces.Business.Entities.ICRUDBusiness import ICRUDBusiness
from typing import TypeVar, Generic, Type

T = TypeVar('T')

class CRUDBusiness(Generic[T], ICRUDBusiness):
    Session = Session()
    model: Type[T]

    def __init__(self, model: Type[T]):
        self.model = model

    def Create(self, model):
        try:
            self.Session.add(model)
            self.Session.commit()
        except Exception as e:
            print('Exception to create model ', e)
            self.Session.rollback()

    def Get(self):
        return self.Session.query(self.model).all()

    def GetById(self, id:int):
        return self.Session.query(self.model).filter(self.model.id == id).first()

    def Update(self, model):
        raise NotImplementedError()

    def Delete(self, model):
        raise NotImplementedError()
