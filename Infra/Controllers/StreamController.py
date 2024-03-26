import time

from flask import Blueprint, Response

from Application.Services.Events.StreamService import StreamService
from Infra.Controllers.BaseController import BaseController
from Infra.Views.Response.ExceptionView import ExceptionView

streamBlueprint = Blueprint('stream', __name__, url_prefix='/stream')


class StreamController(BaseController):

    @staticmethod
    @streamBlueprint.route('/Connect', methods=['GET'])
    def Connect():
        try:
            service = StreamService()
            return service.HandleConnect()
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))
