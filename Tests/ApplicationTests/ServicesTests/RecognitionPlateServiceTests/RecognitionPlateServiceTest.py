import pytest
from Application.Services.Recognition.RecognitionPlateService import RecognitionPlateService

def test_get_text_from_plate():
    recognition_plate_service = RecognitionPlateService()
    assert recognition_plate_service.GetTextPlateFromImage() == 'a'