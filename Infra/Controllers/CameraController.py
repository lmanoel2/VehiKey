from flask import Blueprint, request
from pydantic import ValidationError
from Domain.Model.CameraModel import CameraModel
from Domain.Utils.ConverterUtils import ParseObjectToClass, ParseModelToResponseView
from Infra.Controllers.BaseController import BaseController
from Domain.Entities.Camera import Camera
from Infra.Views.Request.CameraRequestView import CameraRequestView
from Application.Services.Entities.CameraService import CameraService
from Infra.Views.Response.ExceptionView import ExceptionView
from Infra.Views.Response.MissingFieldsView import MissingFieldsView
from Infra.Views.Response.CameraResponseView import CameraResponseView

cameraBlueprint = Blueprint('camera', __name__, url_prefix='/camera')


class CameraController(BaseController):
    @staticmethod
    @cameraBlueprint.route('/', methods=['POST'])
    def Create():
        try:
            service = CameraService()
            cameraView = CameraRequestView.parse_raw(request.data)

            newCamera = ParseObjectToClass(cameraView, Camera)

            service.Create(newCamera)

            cameraResponseView = ParseModelToResponseView(newCamera, CameraResponseView)

            return BaseController.ReturnHttpOk(cameraResponseView)
        except ValidationError as e:
            return BaseController.ReturnHttpNotAcceptable(MissingFieldsView(e))
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @cameraBlueprint.route('/', methods=['GET'])
    def Get():
        try:
            service = CameraService()

            cameras = service.Get()

            cameraResponseViews = [ParseModelToResponseView(camera, CameraResponseView)
                                   for camera in cameras]

            return BaseController.ReturnHttpOk(cameraResponseViews)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @cameraBlueprint.route('/<int:id>', methods=['GET'])
    def GetById(id):
        try:
            service = CameraService()

            camera = service.GetById(id)

            cameraResponseView = ParseModelToResponseView(camera, CameraResponseView) if camera else None

            return BaseController.ReturnHttpOk(cameraResponseView)
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @cameraBlueprint.route('/<int:id>', methods=['PUT'])
    def Update(id):
        try:
            service = CameraService()
            cameraView = CameraRequestView.parse_raw(request.data)

            camera = CameraModel(**cameraView.dict())

            updatedCamera = service.Update(id, camera)

            cameraResponseView = CameraResponseView(updatedCamera.id, updatedCamera.ip,
                                                    updatedCamera.port, updatedCamera.password,
                                                    updatedCamera.user, updatedCamera.name,
                                                    updatedCamera.manufacturer, updatedCamera.valid_time) \
                if updatedCamera else None

            return BaseController.ReturnHttpOk(cameraResponseView)
        except ValidationError as e:
            return BaseController.ReturnHttpNotAcceptable(MissingFieldsView(e))
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))

    @staticmethod
    @cameraBlueprint.route('/<int:id>', methods=['DELETE'])
    def DeleteById(id):
        try:
            service = CameraService()

            deletedCamera = service.DeleteById(id)

            cameraResponseView = ParseModelToResponseView(deletedCamera, CameraResponseView) \
                if deletedCamera else None

            return BaseController.ReturnHttpOk(cameraResponseView)
        except BaseException as e:
            return BaseController.ReturnHttpNotAcceptable(ExceptionView(e))
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))
