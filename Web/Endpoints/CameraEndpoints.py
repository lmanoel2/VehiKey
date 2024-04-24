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

    def UpdateCamera(self, dataPut):
        urlFormatted = f"{self.url}/{dataPut['id']}"

        model = CameraModel(name=dataPut['name'],
                            ip=dataPut['ip'],
                            port=dataPut['port'],
                            user=dataPut['user'],
                            password=dataPut['password'],
                            controller=dataPut['controller'],
                            manufacturer='INTELBRAS')
        data = dict(model)
        requests.put(urlFormatted, json=data)

        return dataPut

    def DeleteCamera(self, id: int):
        urlFormatted = f"{self.url}/{id}"
        requests.delete(urlFormatted)

    def AddRange(self, request):
        names = request.POST.getlist('name')
        ips = request.POST.getlist('ip')
        ports = request.POST.getlist('port')
        users = request.POST.getlist('user')
        passwords = request.POST.getlist('password')
        controllers = request.POST.getlist('controller')

        for name, ip, port, user, password, controller in zip(names, ips, ports, users, passwords, controllers):
            model = CameraModel(name=name,
                                ip=ip,
                                port=port,
                                user=user,
                                password=password,
                                manufacturer='INTELBRAS',
                                controller=controller)
            data = dict(model)
            requests.post(self.url, json=data)

        return zip(names, ips, ports, users, passwords)