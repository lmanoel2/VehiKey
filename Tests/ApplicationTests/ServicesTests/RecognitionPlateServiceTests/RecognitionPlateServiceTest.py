import cv2
import os
from Application.Services.Recognition.RecognitionPlateService import RecognitionPlateService

parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def testGetTextPlateOldFromImage():
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')
    image = cv2.imread(directoryImage)
    recognitionPlateService = RecognitionPlateService()

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'LPM9710'
    assert plateScore > 0.07

def testGetTextPlateNewFromImage():
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithNewPlate.jpg')
    image = cv2.imread(directoryImage)
    recognitionPlateService = RecognitionPlateService()

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'BEE4R22'
    assert plateScore > 0.64
