import json
import os
import requests
import sys

from Domain.Model.VehicleModel import VehicleModel

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)


class VehicleEndpoints:
    url = 'http://127.0.0.1:5000/vehicle'

    def GetAllVehicles(self):
        responseString = (requests.get(self.url)).content.decode('utf-8')
        data = json.loads(responseString)
        return data

    def GetVehicleById(self, id: int):
        urlFormatted = f"{self.url}/{id}"
        responseString = (requests.get(urlFormatted)).content.decode('utf-8')
        data = json.loads(responseString)
        return data

    def AddRange(self, request):
        colors = request.POST.getlist('color')
        plates = request.POST.getlist('plate')

        for color, plate in zip(colors, plates):
            model = VehicleModel(color=color,
                                 plate=plate)
            data = dict(model)
            requests.post(self.url, json=data)

        return zip(colors, plates)
