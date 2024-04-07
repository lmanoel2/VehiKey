import json
import os
import requests
import sys

from Domain.Model.CameraModel import CameraModel

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)


class CameraEndpoints:
    url = 'http://127.0.0.1:5000/camera'

    def GetAllCameras(self):
        responseString = (requests.get(self.url)).content.decode('utf-8')
        data = json.loads(responseString)
        return data

    def GetCameraById(self, id: int):
        urlFormatted = f"{self.url}/{id}"
        responseString = (requests.get(urlFormatted)).content.decode('utf-8')
        data = json.loads(responseString)
        return data

    def AddRange(self, request):
        names = request.POST.getlist('name')
        ips = request.POST.getlist('ip')
        ports = request.POST.getlist('port')
        users = request.POST.getlist('user')
        passwords = request.POST.getlist('password')

        for name, ip, port, user, password in zip(names, ips, ports, users, passwords):
            model = CameraModel(name=name,
                                ip=ip,
                                port=port,
                                user=user,
                                password=password,
                                manufacturer='INTELBRAS')
            data = dict(model)
            requests.post(self.url, json=data)

        return zip(names, ips, ports, users, passwords)