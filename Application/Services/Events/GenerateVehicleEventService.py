from Application.Business.Entities.EventBusiness import EventBusiness
from Domain.Interfaces.Services.Events.IGenerateVehicleEventService import IGenerateVehicleEventService
from Domain.Model.Events.Vehicle.VehicleEventModel import *
from Domain.Entities.Event import Event


class GenerateVehicleEventService(IGenerateVehicleEventService):
    business = EventBusiness()

    def SendVehicleNotFound(self, plate: str):
        print('Vehicle not found')
        message = VehicleNotFound().json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleOK(self, plate: str):
        print('Vehicle OK')
        message = VehicleOk().json()
        event = Event(message=message)
        self.business.Create(event)
