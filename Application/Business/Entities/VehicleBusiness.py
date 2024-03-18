from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Application.Exceptions.Entities.VehicleExceptions import PlateAlreadyExistsError
from Domain.Entities.Vehicle import Vehicle


class VehicleBusiness(CRUDBusiness):
    def __init__(self):
        super().__init__(Vehicle)

    def Create(self, model: Vehicle):
        self.__AlreadyExistePlate(model.plate)
        super().Create(model)

    def GetByPlate(self, plate: str) -> Vehicle:
        return self.Session.query(Vehicle).filter(Vehicle.plate == plate).first()

    def __AlreadyExistePlate(self, plate: str):
        alreadyExistPlate = bool(self.GetByPlate(plate))

        if alreadyExistPlate:
            raise PlateAlreadyExistsError()

