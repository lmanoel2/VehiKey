import json

from Application.Business.Entities.CameraBusiness import CameraBusiness
from Application.Business.Entities.EventBusiness import EventBusiness
from Domain.Entities.Event import Event
from Domain.Interfaces.Services.Events.ISaveEventService import ISaveEventService
from Domain.Model.Events.HardwareExternal.HardwareExternalEventModel import DoorStatus


class SaveEventService(ISaveEventService):
    cameraBusiness = CameraBusiness()
    eventBusiness = EventBusiness()

    def SaveEvent(self, event: str, serialNumber: str):

        if serialNumber is None or serialNumber == "":
            return

        if event is None or event == "":
            return

        try:
            json_data = json.loads(event)
            print(json_data)
        except json.JSONDecodeError as e:
            print("Error:", e)
            return

        camera = self.cameraBusiness.GetByController(serialNumber)
        code = json_data.get('code', -1)

        message = DoorStatus(code=code, from_controller=serialNumber, from_camera=camera.id).json()

        print(f'Saving event => {message}')
        event = Event(message=message)
        self.eventBusiness.Create(event)
