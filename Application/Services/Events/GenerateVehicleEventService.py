from Domain.Interfaces.Services.Events.IGenerateVehicleEventService import IGenerateVehicleEventService


class GenerateVehicleEventService(IGenerateVehicleEventService):
    def SendVehicleNotFound(self, plate: str):
        print('Vehicle not found')

    def SendVehicleOK(self, plate: str):
        print('Vehicle OK')