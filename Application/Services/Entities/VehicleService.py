from Application.Business.Entities.VehicleBusiness import VehicleBusiness
from Domain.Entities.Vehicle import Vehicle
from Domain.Interfaces.Services.Entities.IVehicleService import IVehicleService


class VehicleService(IVehicleService):
    def Create(self, vehicle: Vehicle):
        business = VehicleBusiness()
        return business.Create(vehicle)

