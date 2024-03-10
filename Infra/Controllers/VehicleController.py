from flask import Blueprint, request

from Infra.Controllers.BaseController import BaseController
from Infra.Controllers.CRUDController import CRUDController
from Domain.DataBase.Context import Session
from Domain.Entities.Vehicle import Vehicle
from Infra.Views.Request.VehicleView import VehicleView
from Application.Services.Entities.VehicleService import VehicleService
from Infra.Views.Response.ExceptionView import ExceptionView
import json

vehicleBlueprint = Blueprint('vehicle', __name__, url_prefix='/vehicle')

class VehicleController(CRUDController):
    @vehicleBlueprint.route('/')
    @staticmethod
    def Read():
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

    @vehicleBlueprint.route('/', methods=['POST'])
    @staticmethod
    def Create():
        vehicleView = VehicleView.parse_raw(request.data)
        newVehicle = Vehicle(color=vehicleView.color, model=vehicleView.model, plate=vehicleView.plate)
        service = VehicleService()

        try:
            return service.Create(newVehicle)
        except Exception as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))

