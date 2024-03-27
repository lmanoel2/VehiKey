from datetime import datetime

from flask import Response
from Domain.Interfaces.Services.Events.IStreamService import IStreamService
from Application.Business.Entities.EventBusiness import EventBusiness


class StreamService(IStreamService):
    EventBusiness = EventBusiness()

    def __init__(self):
        self.Boundary = "--boundary"
        self.LastDateKeepAlive = datetime.now()

    def HandleConnect(self):
        return Response(self.GenerateMessages(), content_type=f'multipart/mixed; boundary={self.Boundary}')

    def GenerateMessages(self):
        yield f"{self.Boundary}\n"
        yield "Content-Type: application/json\n\n"
        yield "Keep alive\n\n"

        while True:
            events = self.EventBusiness.GetEventsNotSent()

            for event in events:
                if self.ShouldSendKeepAlive():
                    yield f"{self.Boundary}\n"
                    yield "Content-Type: application/json\n\n"
                    yield "Keep alive\n\n"

                yield f"--{self.Boundary}\n"
                yield "Content-Type: application/json\n\n"
                yield f"{event.message}\n\n"

            if self.ShouldSendKeepAlive():
                yield f"{self.Boundary}\n"
                yield "Content-Type: application/json\n\n"
                yield "Keep alive\n\n"

    def ShouldSendKeepAlive(self):
        t = datetime.now()
        elapsedTime = t - self.LastDateKeepAlive
        totalSe = elapsedTime.total_seconds()
        if totalSe < 30:
            return False

        self.LastDateKeepAlive = datetime.now()
        return True
