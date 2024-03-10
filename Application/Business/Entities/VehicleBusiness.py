from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Application.Exceptions.Entities.VehicleExceptions import PlateAlreadyExistsError
from Domain.Entities.Vehicle import Vehicle


class VehicleBusiness(CRUDBusiness):

    def Create(self, model: Vehicle):
        self.__AlreadyExistePlate(model.plate)
        self.Session.add(model)
        self.Session.commit()

    def __AlreadyExistePlate(self, plate: str):
        alreadyExistPlate = bool(self.Session.query(Vehicle).filter(Vehicle.plate == plate).first())

        if (alreadyExistPlate):
            raise PlateAlreadyExistsError()

