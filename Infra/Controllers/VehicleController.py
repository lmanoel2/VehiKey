from flask import Blueprint

vehicleBlueprint = Blueprint('vehicle', __name__)

@vehicleBlueprint.route('/testeVehicle')
def get_vehicles():
    return "Acessado vehicle"