import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from flask import Flask
from Infra.Configs.Startup.StartupConfig import RegisterBlueprints
from Infra.Configs.Startup.DatabaseStartup import CreateOrCheckDatabase
from Application.Services.Video.CameraService import CameraService
from Application.Services.Mqtt.ClientMqtt import clientPubSub
from Domain.Entities.Camera import Camera

print("Starting...")
app = Flask(__name__)

CreateOrCheckDatabase()
RegisterBlueprints(app)

clientPubSub.Start()

# camera = Camera('admin','admin123','10.0.0.106')
# cameraService = CameraService(camera)
# cameraService.StartStream()

if __name__ == '__main__':
    app.run(debug=False)
