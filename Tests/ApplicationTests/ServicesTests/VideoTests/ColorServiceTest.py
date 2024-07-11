import os

import cv2

from Application.Services.Video.ColorService import ColorService

parentDirectoryTest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def testGetColorCarSilver():
    #Arrange
    colorService = ColorService()
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'carroPrata.jpg')
    image = cv2.imread(directoryImage)

    #Act
    color = colorService.GetColorFromImage(image)

    #Assert
    assert color == 'Silver'

def testGetColorCarBlack():
    #Arrange
    colorService = ColorService()
    directoryImage = os.path.join(parentDirectoryTest, 'UtilsTests', 'Photos', 'preto.png')
    image = cv2.imread(directoryImage)

    #Act
    color = colorService.GetColorFromImage(image)

    #Assert
    assert color == 'Black'
