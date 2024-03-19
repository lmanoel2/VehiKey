import pytest
from Application.Services.Events.GenerateVehicleEventService import GenerateVehicleEventService


@pytest.mark.parametrize("generateVehicleEventService", [GenerateVehicleEventService()])
def testSendVehicleOK(generateVehicleEventService):
    # Arrange
    plate = 'QJI0643'

    # Act
    generateVehicleEventService.SendVehicleOK(plate)

@pytest.mark.parametrize("generateVehicleEventService", [GenerateVehicleEventService()])
def testSendVehicleNotFound(generateVehicleEventService):
    # Arrange
    plate = 'QJI0643'

    # Act
    generateVehicleEventService.SendVehicleNotFound(plate)

