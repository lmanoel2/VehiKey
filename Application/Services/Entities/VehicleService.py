from Application.Business.Entities.VehicleBusiness import VehicleBusiness
from Domain.Entities.Vehicle import Vehicle
from Domain.Interfaces.Services.Entities.IVehicleService import IVehicleService
from Domain.Model.VehicleModel import VehicleModel


class VehicleService(IVehicleService):
    business = VehicleBusiness()

    def Create(self, vehicle: Vehicle):
        return self.business.Create(vehicle)

    def Get(self):
        return self.business.Get()

    def GetById(self, id: int):
        return self.business.GetById(id)

    def Update(self, id: int, model: VehicleModel):
        return self.business.Update(id, model)

    def DeleteById(self, id: int):
        return self.business.DeleteById(id)
