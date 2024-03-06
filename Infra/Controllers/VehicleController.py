from flask import Blueprint
from Infra.Controllers.CRUDController import CRUDController
from Domain.DataBase.Context import Session
from Domain.Entities.Vehicle import Vehicle

vehicleBlueprint = Blueprint('vehicle', __name__, url_prefix='/vehicle')

class VehicleController(CRUDController):

    @vehicleBlueprint.route('/')
    @staticmethod
    def read():
        session = Session()

        try:
            red_vehicles = session.query(Vehicle).filter(Vehicle.color == 'vermelha').all()

            # Itere sobre os resultados, se necessário
            for vehicle in red_vehicles:
                return vehicle.model

        except Exception as e:
            print("Erro ao consultar o banco de dados utilizando SQL Raw:", e)

        finally:
            # Feche a sessão
            session.close()

        return CRUDController.read()
