import requests, json, os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Domain.Model.CameraModel import CameraModel


class CameraEndpoints:
    url = 'http://127.0.0.1:5000/camera'

    def GetAllCameras(self):
        responseString = (requests.get(self.url)).content.decode('utf-8')
        data = json.loads(responseString)
        cameras = [CameraModel(**item) for item in data]
        return cameras
