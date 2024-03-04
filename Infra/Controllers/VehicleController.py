from flask import Blueprint
from Infra.Controllers.CRUDController import CRUDController

vehicleBlueprint = Blueprint('vehicle', __name__)


class VehicleController(CRUDController):

    @vehicleBlueprint.route('/testeVehicle')
    @staticmethod
    def read():
        return CRUDController.read()
