import cv2
import os
import pytest
from Application.Services.Video.RecognitionPlateService import RecognitionPlateService

parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


@pytest.mark.parametrize("recognitionPlateService", [RecognitionPlateService()])
def testGetTextPlateOldFromImage(recognitionPlateService):
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')
    image = cv2.imread(directoryImage)

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'LPM9710'
    assert plateScore > 0.07


@pytest.mark.parametrize("recognitionPlateService", [RecognitionPlateService()])
def testGetTextPlateNewFromImage(recognitionPlateService):
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithNewPlate.jpg')
    image = cv2.imread(directoryImage)

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'BEE4R22'
    assert plateScore > 0.64


@pytest.mark.parametrize("recognitionPlateService", [RecognitionPlateService()])
def testGetNoneTextFromImageWithPlateNotValid(recognitionPlateService):
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithPlateNotValid.jpg')
    image = cv2.imread(directoryImage)

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText is None
    assert plateScore is None
