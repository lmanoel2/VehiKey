from flask import Blueprint, request
from pydantic import ValidationError
from Infra.Controllers.BaseController import BaseController
from Domain.DataBase.Context import Session
from Domain.Entities.Vehicle import Vehicle
from Infra.Views.Request.VehicleRequestView import VehicleRequestView
from Application.Services.Entities.VehicleService import VehicleService
from Infra.Views.Response.ExceptionView import ExceptionView
from Infra.Views.Response.MissingFieldsView import MissingFieldsView
from Infra.Views.Response.VehicleResponseView import VehicleResponseView

vehicleBlueprint = Blueprint('vehicle', __name__, url_prefix='/vehicle')


class VehicleController(BaseController):
    @staticmethod
    @vehicleBlueprint.route('/', methods=['POST'])
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

    @staticmethod
    @vehicleBlueprint.route('/', methods=['get'])
    def Get():
        try:
            service = VehicleService()

            vehicles = service.Get()

            vehicleResponseViews = [VehicleResponseView(vehicle.id, vehicle.color, vehicle.plate)
                                    for vehicle in vehicles]

            return BaseController.ReturnHttpOk(vehicleResponseViews)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @vehicleBlueprint.route('/<int:id>', methods=['get'])
    def GetById(id):
        try:
            service = VehicleService()

            vehicle = service.GetById(id)

            vehicleResponseView = VehicleResponseView(vehicle.id, vehicle.color, vehicle.plate) if vehicle else None

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))