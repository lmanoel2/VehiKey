from flask import Blueprint
from Infra.Controllers.CRUDController import CRUDController

vehicleBlueprint = Blueprint('vehicle', __name__, url_prefix='/vehicle')

class VehicleController(CRUDController):

    @vehicleBlueprint.route('/')
    @staticmethod
    def read():
        return CRUDController.read()
