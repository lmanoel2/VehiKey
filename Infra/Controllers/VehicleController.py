from flask import Blueprint, request
from pydantic import ValidationError
from Domain.Model.VehicleModel import VehicleModel
from Domain.Utils.ConverterUtils import ParseObjectToClass, ParseModelToResponseView
from Infra.Controllers.BaseController import BaseController
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

            newVehicle = ParseObjectToClass(vehicleView, Vehicle)

            service.Create(newVehicle)

            vehicleResponseView = ParseModelToResponseView(newVehicle, VehicleResponseView)

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except ValidationError as e:
            return BaseController.ReturnHttpNotAcceptable(MissingFieldsView(e))
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @vehicleBlueprint.route('/', methods=['GET'])
    def Get():
        try:
            service = VehicleService()

            vehicles = service.Get()

            vehicleResponseViews = [ParseModelToResponseView(vehicle, VehicleResponseView)
                                    for vehicle in vehicles]

            return BaseController.ReturnHttpOk(vehicleResponseViews)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @vehicleBlueprint.route('/<int:id>', methods=['GET'])
    def GetById(id):
        try:
            service = VehicleService()

            vehicle = service.GetById(id)

            vehicleResponseView = ParseModelToResponseView(vehicle,VehicleResponseView) if vehicle else None

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @vehicleBlueprint.route('/<int:id>', methods=['PUT'])
    def Update(id):
        try:
            service = VehicleService()
            vehicleView = VehicleRequestView.parse_raw(request.data)

            vehicle = VehicleModel(**vehicleView.dict())

            updatedVehicle = service.Update(id, vehicle)

            vehicleResponseView = VehicleResponseView(updatedVehicle.id, updatedVehicle.color, updatedVehicle.plate) if updatedVehicle else None

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except ValidationError as e:
            return BaseController.ReturnHttpNotAcceptable(MissingFieldsView(e))
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @vehicleBlueprint.route('/<int:id>', methods=['DELETE'])
    def DeleteById(id):
        try:
            service = VehicleService()

            deletedVehicle = service.DeleteById(id)

            vehicleResponseView = ParseModelToResponseView(deletedVehicle, VehicleResponseView) \
                if deletedVehicle else None

            return BaseController.ReturnHttpOk(vehicleResponseView)
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))