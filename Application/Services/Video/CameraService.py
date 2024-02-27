import cv2
from ultralytics import YOLO
from Domain.Entities.Camera import Camera
from Domain.Interfaces.Services.Video.ICameraService import ICameraService
from Domain.Enumerators.Recognition.YoloModels import YoloModels


class CameraService(ICameraService):
    maxFrame = 30

    def StartStream(self, camera: Camera):
        print("Starting video stream...")

        vehicles = [YoloModels.MOTORCYCLE.value, YoloModels.BUS.value, YoloModels.CAR.value, YoloModels.TRUCK.value,                    YoloModels]
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

                detectionsVehicles = model(frame, verbose=False)[0]

                for detectionsVehicle in detectionsVehicles.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = detectionsVehicle
                    if int(class_id) in vehicles:
                        print(f'vehicle detected {YoloModels(class_id).name} with score {score}')

        cap.release()


if __name__ == '__main__':
    camera = Camera('admin', 'admin123', '10.0.0.106')
    cameraService = CameraService()
    cameraService.StartStream(camera)
