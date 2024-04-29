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
        connection = self.Session.bind.raw_connection()

        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM event WHERE sent_to_server = 0"
            cursor.execute(query)
            events = cursor.fetchall()
            cursor.close()

            if events:
                update_query = "UPDATE event SET sent_to_server = 1 WHERE sent_to_server = 0"
                cursor = connection.cursor()
                cursor.execute(update_query)
                connection.commit()
                cursor.close()

            return events
        finally:
            connection.close()

    def SetEventsToSent(self, events: List[Event]):
        for event in events:
            event.sent_to_server = True
            model = EventModel(message=event.message, sent_to_server=event.sent_to_server)
            super().Update(event.id, model)
