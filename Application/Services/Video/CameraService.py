import cv2
from ultralytics import YOLO

from Application.Services.AccessControl.AccessControlService import AccessControlService
from Domain.Entities.Camera import Camera
from Domain.Interfaces.Services.Video.ICameraService import ICameraService
from Domain.Enumerators.Recognition.YoloModels import YoloModels
from Application.Services.Video.RecognitionPlateService import RecognitionPlateService


class CameraService(ICameraService):
    maxFrame = 30

    def StartStream(self, camera: Camera):
        print("Starting video stream...")
        recognitionPlateService = RecognitionPlateService()

        vehicles = [YoloModels.MOTORCYCLE.value, YoloModels.BUS.value, YoloModels.CAR.value, YoloModels.TRUCK.value,
                    YoloModels]
        rtspUrl = f'rtsp://{camera.user}:{camera.password}@{camera.ip}:554/cam/realmonitor?channel=1&subtype=0'
        model = YOLO('yolov8n.pt')

        frameCount = -1

        cap = cv2.VideoCapture(rtspUrl)

        if not cap.isOpened():
            print(f"Unable to connect to camera {rtspUrl}")
            return

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error receiving frame")
                break

            frameCount += 1
            if ret and frameCount > self.maxFrame:
                frameCount = 0
                self.__ProcessFrame(frame, model, recognitionPlateService, vehicles)

        cap.release()

    @staticmethod
    def PrintFrame(frame):
        cv2.imshow('Frame', frame)
        cv2.waitKey(1)

    def __ProcessFrame(self, frame, model, recognitionPlateService, vehicles):
        #self.PrintFrame(frame) #Retire o comentario para ver o video em tempo real
        detectionsVehicles = model(frame, verbose=False)[0]
        for detectionsVehicle in detectionsVehicles.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detectionsVehicle
            x1 = int(round(x1))
            y1 = int(round(y1))
            x2 = int(round(x2))
            y2 = int(round(y2))

            if int(class_id) in vehicles:
                #print(f'vehicle detected {YoloModels(class_id).name} with score {score}')
                croppedImage = frame[y1:y2, x1:x2]
                licensePlate, licenseScore = recognitionPlateService.GetTextPlateFromImage(croppedImage)
                print(licensePlate, licenseScore)

                if licensePlate:
                    accessControlService = AccessControlService()
                    accessControlService.ProcessPlate(licensePlate, licenseScore)

if __name__ == '__main__':
    camera = Camera('admin', 'admin123', '10.0.0.106')
    cameraService = CameraService()
    cameraService.StartStream(camera)
