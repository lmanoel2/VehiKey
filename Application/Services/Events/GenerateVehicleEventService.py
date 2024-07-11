from Application.Business.Entities.EventBusiness import EventBusiness
from Domain.Interfaces.Services.Events.IGenerateVehicleEventService import IGenerateVehicleEventService
from Domain.Model.Events.Vehicle.VehicleEventModel import *
from Domain.Entities.Event import Event


class GenerateVehicleEventService(IGenerateVehicleEventService):
    business = EventBusiness()

    def SendVehicleOK(self, plate: str, color):
        print(f'Vehicle OK {plate} - {color}')
        message = VehicleOk(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleNotFound(self, plate, color):
        print(f'Vehicle not found {plate} - {color}')
        message = VehicleNotFound(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleOutOfHour(self, plate: str, color):
        print(f'Vehicle out of hour {plate} - {color}')
        message = VehicleOutOfHour(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)

    def SendVehicleWithCameraOutOfHour(self, plate: str, color):
        print(f'Vehicle with camera out of hour {plate} - {color}')
        message = VehicleWithCameraOutOfHour(plate=plate).json()
        event = Event(message=message)
        self.business.Create(event)
