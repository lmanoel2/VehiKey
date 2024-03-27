from typing import List
from Application.Business.Entities.CRUDBusiness import CRUDBusiness
from Domain.Entities.Event import Event
from Domain.Model.EventModel import EventModel


class EventBusiness(CRUDBusiness):
    def __init__(self):
        super().__init__(Event)

    def Create(self, model: Event):
        super().Create(model)

    def GetEventsNotSent(self) -> List[Event]:
        events = self.Session.query(Event).filter(Event.sent_to_server == 0).all()
        self.SetEventsToSent(events)
        return events

    def SetEventsToSent(self, events: List[Event]):
        for event in events:
            event.sent_to_server = True
            model = EventModel(message=event.message, sent_to_server=event.sent_to_server)
            super().Update(event.id, model)
