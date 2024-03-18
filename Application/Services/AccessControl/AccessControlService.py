from Application.Services.Events.GenerateVehicleEventService import GenerateVehicleEventService
from Domain.Interfaces.Services.AccessControl.IAccessControlService import IAccessControlService
from Application.Business.Entities.VehicleBusiness import VehicleBusiness


class AccessControlService(IAccessControlService):
    business = VehicleBusiness()
    generateVehicleEvent = GenerateVehicleEventService()

    def ProcessPlate(self, plate: str, plateScore: float):
        vehicle = self.business.GetByPlate(plate)

        if not bool(vehicle):
            self.generateVehicleEvent.SendVehicleNotFound(plate)
            return

        self.generateVehicleEvent.SendVehicleOK(plate)
