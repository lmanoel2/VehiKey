from flask import Blueprint, request
from Application.Services.Mqtt.ClientMqtt import clientPubSub
from Infra.Controllers.BaseController import BaseController
from Infra.Views.Response.ExceptionView import ExceptionView

streamBlueprint = Blueprint('pubsub', __name__, url_prefix='/pubsub')


class StreamController(BaseController):

    @staticmethod
    @streamBlueprint.route('/publish', methods=['POST'])
    def Publish():
        try:
            clientPubSub.Publish(request.data)
            return BaseController.ReturnHttpOk('')
        except Exception as e:
            return BaseController.ReturnHttpBadRequest(ExceptionView(e))
