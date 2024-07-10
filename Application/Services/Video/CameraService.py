import cv2
import time
from ultralytics import YOLO

from Application.Services.AccessControl.AccessControlService import AccessControlService
from Domain.Entities.Camera import Camera
from Domain.Interfaces.Services.Video.ICameraService import ICameraService
from Domain.Enumerators.Recognition.YoloModels import YoloModels
from Application.Services.Video.RecognitionPlateService import RecognitionPlateService


class CameraService(ICameraService):
    maxFrame = 30

    def StartStream(self):
        print("Starting video stream...")
        recognitionPlateService = RecognitionPlateService()

        vehicles = [YoloModels.MOTORCYCLE.value, YoloModels.BUS.value, YoloModels.CAR.value, YoloModels.TRUCK.value,
                    YoloModels]
        rtspUrl = f'rtsp://{self.camera.user}:{self.camera.password}@{self.camera.ip}:554/cam/realmonitor?channel=1&subtype=0'
        model = YOLO('yolov8n.pt')

        while True:
            cap = cv2.VideoCapture(rtspUrl)

            if not cap.isOpened():
                print(f"Unable to connect to camera {rtspUrl}")
                return

            ret, frame = cap.read()
            cap.release()

            if not ret:
                print("Error receiving frame")
                break

            self.ProcessFrame(frame, model, recognitionPlateService, vehicles)

            cap.release()
            time.sleep(1)

    @staticmethod
    def PrintFrame(frame):
        cv2.imshow('Frame', frame)
        cv2.waitKey(1)

    def ProcessFrame(self, frame, model, recognitionPlateService, vehicles):
        #self.PrintFrame(frame)  # Retire o comentario para ver o video em tempo real
        detectionsVehicles = model(frame, verbose=False)[0]
        for detectionsVehicle in detectionsVehicles.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detectionsVehicle
            x1 = int(round(x1))
            y1 = int(round(y1))
            x2 = int(round(x2))
            y2 = int(round(y2))

            if int(class_id) in vehicles:
                croppedImage = frame[y1:y2, x1:x2]
                #self.PrintFrame(croppedImage)

                licensePlate, licenseScore = recognitionPlateService.GetTextPlateFromImage(croppedImage)
                print(licensePlate, licenseScore)

                if licensePlate:
                    accessControlService = AccessControlService(self.camera)
                    accessControlService.ProcessPlate(licensePlate, licenseScore)

    def __init__(self, camera: Camera):
        self.camera = camera


if __name__ == '__main__':
    camera = Camera('admin', 'admin123', '10.0.0.106')
    cameraService = CameraService(camera)
    cameraService.StartStream()
