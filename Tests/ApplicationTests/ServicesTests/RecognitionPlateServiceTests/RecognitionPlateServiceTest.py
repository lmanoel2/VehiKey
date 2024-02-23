import cv2
import os
from Application.Services.Recognition.RecognitionPlateService import RecognitionPlateService


def test_get_text_plate_old_from_image():
    # Arrange
    parent_directory_test = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    directory_image = os.path.join(parent_directory_test, 'UtilsTests', 'Photos', 'CarWithOldPlate.jpg')
    image = cv2.imread(directory_image)
    recognition_plate_service = RecognitionPlateService()

    # Act
    plateText = recognition_plate_service.GetTextPlateFromImage(image)

    # Assert
    assert plateText == 'LPM9710'
