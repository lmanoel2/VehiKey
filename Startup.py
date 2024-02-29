from Domain.Entities.Camera import Camera
from Application.Services.Video.CameraService import CameraService

print("Starting...")

camera = Camera('admin', 'admin123', '10.0.0.106')
cameraService = CameraService()
cameraService.StartStream(camera)

print("Finish")