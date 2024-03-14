import json

from flask import make_response
from Domain.Utils.ConverterUtils import ParseClassToJson, ParseClassToDict


class BaseController:
    @staticmethod
    def ReturnHttpOk(obj):
        if isinstance(obj, str):
            return make_response(obj, 200)
        elif isinstance(obj, list):
            json_message = [ParseClassToDict(item) for item in obj]
            return make_response(json.dumps(json_message), 200)
        else:
            json_message = ParseClassToJson(obj)
            return make_response(json_message, 200)

    @staticmethod
    def ReturnHttpBadRequest(obj):
        if isinstance(obj, str):
            return make_response(obj, 400)
        else:
            json_message = ParseClassToJson(obj)
            return make_response(json_message, 400)

    @staticmethod
    def ReturnHttpNotAcceptable(obj):
        if isinstance(obj, str):
            return make_response(obj, 406)
        else:
            json_message = ParseClassToJson(obj)
            return make_response(json_message, 406)

    @staticmethod
    def ReturnHttpMissingFields(obj):
        missingFields = [error["loc"][0] for error in obj.errors()]
        return make_response(missingFields, 422)
