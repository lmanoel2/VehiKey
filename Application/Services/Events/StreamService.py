import time
import threading
from flask import Response
from Domain.Interfaces.Services.Events.IStreamService import IStreamService


class StreamService(IStreamService):

    def __init__(self):
        self.boundary = "--boundary"

    def HandleConnect(self):
        return Response(self.GenerateMessages(), content_type=f'multipart/mixed; boundary={self.boundary}')

    def GenerateMessages(self):
        while True:
            # Aqui você pode chamar a função do seu serviço para obter mensagens em tempo real
            message = "Nova mensagem em tempo real"

            yield f"--{self.boundary}\n"
            yield "Content-Type: application/json\n\n"
            yield f"{message}\n\n"

            time.sleep(10)  # Atraso de 1 segundo entre cada mensagem

    def SendKeepAlive(self):
        while True:
            yield f"{self.boundary}\n"
            yield "Content-Type: application/json\n\n"
            yield "Keep alive\n\n"


