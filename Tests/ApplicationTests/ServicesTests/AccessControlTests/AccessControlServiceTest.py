from datetime import datetime, timezone, timedelta

import pytest
from unittest.mock import patch, MagicMock

from Application.Services.AccessControl.AccessControlService import AccessControlService
from Domain.Entities.Camera import Camera
from Domain.Entities.Vehicle import Vehicle


@pytest.fixture
def AccessControlServiceWithMocks():
    accessControlService = AccessControlService(camera=Camera('', '', ''))
    accessControlService.generateVehicleEvent = MagicMock()
    accessControlService.business = MagicMock()
    return accessControlService


def testSendVehicleOKWithoutValidTime(AccessControlServiceWithMocks):
    # Arrange
    vehicle = Vehicle()
    plate = 'QJI0643'
    score = 0.07
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleOK.assert_called_once_with(plate)


def testSendVehicleOKWithValidTimeAllowed(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=-3)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=+2)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    vehicle.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleOK.assert_called_once_with(plate)


def testSendVehicleOutOfHourWithEndTimeOut(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=-3)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=-2)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    vehicle.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleOutOfHour.assert_called_once_with(plate)


def testSendVehicleOutOfHourWithStartTimeOut(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=+3)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=+5)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    vehicle.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleOutOfHour.assert_called_once_with(plate)


def testSendVehicleWithCameraOutOfHourWithEndTimeOut(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=-5)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=-3)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    AccessControlServiceWithMocks.camera.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleWithCameraOutOfHour.assert_called_once_with(plate)


def testSendVehicleWithCameraOutOfHourWithStartTimeOut(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=+2)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=+3)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    AccessControlServiceWithMocks.camera.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleWithCameraOutOfHour.assert_called_once_with(plate)


def testSendVehicleOKWithCameraValidTimeAllowed(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    utcnow = datetime.now(timezone.utc)
    startTime = (utcnow + timedelta(hours=-2)).strftime("%d-%m-%Y-%H:%M")
    endTime = (utcnow + timedelta(hours=+3)).strftime("%d-%m-%Y-%H:%M")
    vehicle = Vehicle()
    AccessControlServiceWithMocks.camera.SetValidTime(f'{startTime} {endTime}')
    AccessControlServiceWithMocks.business.GetByPlate.return_value = vehicle

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleOK.assert_called_once_with(plate)


def testSendVehicleNotFound(AccessControlServiceWithMocks):
    # Arrange
    plate = 'QJI0643'
    score = 0.07
    AccessControlServiceWithMocks.business.GetByPlate.return_value = None

    # Act
    AccessControlServiceWithMocks.ProcessPlate(plate, score)

    # Assert
    AccessControlServiceWithMocks.generateVehicleEvent.SendVehicleNotFound.assert_called_once_with(plate)
