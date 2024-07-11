import os
import cv2
import numpy as np
from PIL import Image

from Application.Services.Video.CameraService import CameraService
from Application.Services.Video.RecognitionPlateService import RecognitionPlateService
from Domain.Entities.Camera import Camera
from ultralytics import YOLO
from Domain.Enumerators.Recognition.YoloModels import YoloModels
parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def testCameraService():
    # Arrange
    camera = Camera('admin', 'admin123', '10.0.0.106')
    cameraService = CameraService(camera)
    recognitionPlateService = RecognitionPlateService()
    model = YOLO('yolov8n.pt')
    vehicles = [YoloModels.MOTORCYCLE.value, YoloModels.BUS.value, YoloModels.CAR.value, YoloModels.TRUCK.value,
                YoloModels]
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')
    #directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')

    image = cv2.imread(directoryImage)

    cameraService.ProcessFrame(image, model, recognitionPlateService, vehicles)