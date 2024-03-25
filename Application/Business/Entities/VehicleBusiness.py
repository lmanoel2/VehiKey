import re
from datetime import datetime, timezone

from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Application.Exceptions.Entities.VehicleExceptions import PlateAlreadyExistsError, ValidTimeNotFormattedError
from Domain.Entities.Vehicle import Vehicle
from Domain.Model.VehicleModel import VehicleModel


class VehicleBusiness(CRUDBusiness):
    def __init__(self):
        super().__init__(Vehicle)

    def Create(self, model: Vehicle):
        self.__AlreadyExistePlate(model.plate)
        self.__ValidateValidTime(model.valid_time)
        super().Create(model)

    def Update(self, id: int, model: VehicleModel):
        vehicle = self.GetById(id)

        if vehicle.plate != model.plate:
            self.__AlreadyExistePlate(model.plate)

        self.__ValidateValidTime(model.valid_time)
        return super().Update(id, model)

    def GetByPlate(self, plate: str) -> Vehicle:
        return self.Session.query(Vehicle).filter(Vehicle.plate == plate).first()

    def __AlreadyExistePlate(self, plate: str):
        alreadyExistPlate = bool(self.GetByPlate(plate))

        if alreadyExistPlate:
            raise PlateAlreadyExistsError()

    def __ValidateValidTime(self, validTime: str):
        if not validTime:
            return

        pattern = r'\d{2}-\d{2}-\d{4}-\d{2}:\d{2} \d{2}-\d{2}-\d{4}-\d{2}:\d{2}'
        patternIsOk = bool(re.match(pattern, validTime))

        if not patternIsOk:
            raise ValidTimeNotFormattedError()

        startDate, endDate = validTime.split()
        datetime.strptime(startDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)
        datetime.strptime(endDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)

