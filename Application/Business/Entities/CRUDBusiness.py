from Application.Exceptions.Entities.BaseException import EntityNotFoundException
from Domain.DataBase.Context import Session
from Domain.Interfaces.Business.Entities.ICRUDBusiness import ICRUDBusiness
from Domain.Utils.ConverterUtils import ParseClassToDict
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
            #self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            raise e

    def Get(self):
        return self.Session.query(self.model).all()

    def GetById(self, id:int):
        return self.Session.query(self.model).filter(self.model.id == id).first()

    def Update(self, id: int, updateData):
        try:
            entity = self.GetById(id)
            updateData = ParseClassToDict(updateData)

            if entity is None:
                raise EntityNotFoundException()

            if isinstance(updateData, dict):
                for key, value in updateData.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
            else:
                for key in [prop for prop in dir(updateData) if
                            not prop.startswith("_") and not callable(getattr(updateData, prop))]:
                    if hasattr(entity, key):
                        value = getattr(updateData, key)
                        setattr(entity, key, value)

            #self.Session.commit()

            return entity
        except Exception as e:
            self.Session.rollback()
            raise e

    def Delete(self, model):
        raise NotImplementedError()

    def DeleteById(self, id: int):
        try:
            entity = self.GetById(id)

            if not entity:
                return None

            self.Session.delete(entity)
            #self.Session.commit()
            return entity
        except Exception as e:
            self.Session.rollback()
            raise e
