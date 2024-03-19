from datetime import datetime, timezone

from Application.Services.Events.GenerateVehicleEventService import GenerateVehicleEventService
from Domain.Entities.Camera import Camera
from Domain.Entities.Vehicle import Vehicle
from Domain.Interfaces.Services.AccessControl.IAccessControlService import IAccessControlService
from Application.Business.Entities.VehicleBusiness import VehicleBusiness


class AccessControlService(IAccessControlService):
    business = VehicleBusiness()
    generateVehicleEvent = GenerateVehicleEventService()

    def ProcessPlate(self, plate: str, plateScore: float):
        vehicle = self.business.GetByPlate(plate)

        if not bool(vehicle):
            self.generateVehicleEvent.SendVehicleNotFound()
            return

        if not AccessControlService.CheckAccessPermissionToVehicle(vehicle):
            self.generateVehicleEvent.SendVehicleOutOfHour(plate)
            return

        self.generateVehicleEvent.SendVehicleOK(plate)

    @staticmethod
    def CheckAccessPermissionToVehicle(vehicle: Vehicle):
        start, end = vehicle.GetValidTime()

        if not AccessControlService.CheckValidTime(start, end):
            return False

        return True

    @staticmethod
    def CheckValidTime(start: datetime, end: datetime):
        utcNow = datetime.now(timezone.utc)
        return start <= utcNow < end

    def __init__(self, camera: Camera):
        self.camera = camera
