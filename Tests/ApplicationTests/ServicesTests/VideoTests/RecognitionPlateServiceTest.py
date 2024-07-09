import cv2
import os
import pytest
from Application.Services.Video.RecognitionPlateService import RecognitionPlateService
import pytesseract
parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))



def test():
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'DusterPlaca2.png')
    image = cv2.imread(directoryImage)
    pytesseract.pytesseract.tesseract_cmd = "D:\Softwares\Pytesseract\Tesseract.exe"
    x = pytesseract.image_to_string(image)
    y = x

@pytest.mark.parametrize("recognitionPlateService", [RecognitionPlateService()])
def testGetTextPlateOldFromImage(recognitionPlateService):
    # Arrange
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')
    image = cv2.imread(directoryImage)

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'LPM9710'
    assert plateScore > 0.69


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

test_data = [
    ('Duster.png', 'CDV2172')
]

@pytest.mark.parametrize("image_file, expected_plate_text", test_data)
def testAnyLicensesPlates(image_file, expected_plate_text):
    # Arrange
    recognitionPlateService = RecognitionPlateService()
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', image_file)
    image = cv2.imread(directoryImage)

    # Act
    plateText, plateScore = recognitionPlateService.GetTextPlateFromImage(image)

    # Assert
    assert plateText == expected_plate_text
