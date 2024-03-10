import json
from flask import make_response


class BaseController:
    @staticmethod
    def ToJson(obj):
        obj_dict = {attr: getattr(obj, attr) for attr in dir(obj) if
                    not attr.startswith("__") and not callable(getattr(obj, attr))}
        return json.dumps(obj_dict)

    @staticmethod
    def ReturnHttpOk(obj):
        if isinstance(obj, str):
            return make_response(obj, 200)
        else:
            json_message = BaseController.ToJson(obj)
            return make_response(json_message, 200)

    @staticmethod
    def ReturnHttpBadRequest(obj):
        if isinstance(obj, str):
            return make_response(obj, 400)
        else:
            json_message = BaseController.ToJson(obj)
            return make_response(json_message, 400)

    @staticmethod
    def ReturnHttpNotAcceptable(obj):
        if isinstance(obj, str):
            return make_response(obj, 406)
        else:
            json_message = BaseController.ToJson(obj)
            return make_response(json_message, 406)

    @staticmethod
    def ReturnHttpMissingFields(obj):
        missingFields = [error["loc"][0] for error in obj.errors()]
        return make_response(missingFields, 422)
