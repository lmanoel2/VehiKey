from Application.Services.Video.CameraService import CameraService
from Domain.Entities.Camera import Camera


def testConnectToCamera():
    # Arrange
    camera = Camera('admin', 'admin123', '10.0.0.106')
    cameraService = CameraService()

    # Act
    cameraService.StartStream(camera)

    # Assert
