from Application.Business.Entities.EventBusiness import EventBusiness
from Domain.Interfaces.Services.Events.IGenerateVehicleEventService import IGenerateVehicleEventService
from Domain.Model.Events.Vehicle.VehicleEventModel import *
from Domain.Entities.Event import Event


class GenerateVehicleEventService(IGenerateVehicleEventService):
    business = EventBusiness()

    def SendVehicleOK(self, plate: str):
        print('Vehicle OK')
        message = VehicleOk(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleNotFound(self, plate):
        print(f'Vehicle not found {plate}')
        message = VehicleNotFound(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleOutOfHour(self, plate: str):
        print('Vehicle out of hour')
        message = VehicleOutOfHour(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleWithCameraOutOfHour(self, plate: str):
        print('Vehicle with camera out of hour')
        message = VehicleWithCameraOutOfHour(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)
