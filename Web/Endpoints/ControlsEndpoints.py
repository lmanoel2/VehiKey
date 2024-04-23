import json
import os
import requests
import sys

from Domain.Model.CameraModel import CameraModel

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)


class ControlsEndpoints:
    url = 'http://127.0.0.1:5000/pubsub'

    def SendCommand(self, action):
        urlFormatted = f"{self.url}/publish"

        requests.post(urlFormatted, data=action)

        return '{"status": "success"}'