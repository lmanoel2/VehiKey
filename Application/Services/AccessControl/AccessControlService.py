from datetime import datetime, timezone

from Application.Services.Events.GenerateVehicleEventService import GenerateVehicleEventService
from Domain.Entities.Camera import Camera
from Domain.Interfaces.Services.AccessControl.IAccessControlService import IAccessControlService
from Application.Business.Entities.VehicleBusiness import VehicleBusiness


class AccessControlService(IAccessControlService):
    business = VehicleBusiness()
    generateVehicleEvent = GenerateVehicleEventService()

    def ProcessPlate(self, plate: str, plateScore: float, color: str):
        vehicle = self.business.GetByPlate(plate)

        if not bool(vehicle):
            self.generateVehicleEvent.SendVehicleNotFound(plate, color)
            return

        if not AccessControlService.CheckAccessPermission(vehicle):
            self.generateVehicleEvent.SendVehicleOutOfHour(plate, color)
            return

        if not AccessControlService.CheckAccessPermission(self.camera):
            self.generateVehicleEvent.SendVehicleWithCameraOutOfHour(plate, color)
            return

        self.generateVehicleEvent.SendVehicleOK(plate, color)

    @staticmethod
    def CheckAccessPermission(entity):
        start, end = entity.GetValidTime()

        if not AccessControlService.CheckValidTime(start, end):
            return False

        return True

    @staticmethod
    def CheckValidTime(start: datetime, end: datetime):
        if not start or not end:
            return True

        utcNow = datetime.now(timezone.utc)
        return start <= utcNow < end

    def __init__(self, camera: Camera):
        self.camera = camera
