from flask import Blueprint, request
from pydantic import ValidationError
from Infra.Controllers.BaseController import BaseController
from Infra.Controllers.CRUDController import CRUDController
from Domain.DataBase.Context import Session
from Domain.Entities.Vehicle import Vehicle
from Infra.Views.Request.VehicleRequestView import VehicleRequestView
from Application.Services.Entities.VehicleService import VehicleService
from Infra.Views.Response.ExceptionView import ExceptionView
from Infra.Views.Response.MissingFieldsView import MissingFieldsView
from Infra.Views.Response.VehicleResponseView import VehicleResponseView

vehicleBlueprint = Blueprint('vehicle', __name__, url_prefix='/vehicle')


class VehicleController(CRUDController):

    @vehicleBlueprint.route('/', methods=['POST'])
    @staticmethod
    def Create():
        try:
            service = VehicleService()
            vehicleView = VehicleRequestView.parse_raw(request.data)

            newVehicle = Vehicle(color=vehicleView.color, plate=vehicleView.plate)

            service.Create(newVehicle)

            vehicleResponseView = VehicleResponseView(newVehicle.id, newVehicle.color, newVehicle.plate)

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except ValidationError as e:
            return BaseController.ReturnHttpNotAcceptable(MissingFieldsView(e))
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @vehicleBlueprint.route('/')
    @staticmethod
    def Get():
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
