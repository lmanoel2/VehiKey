import json
from flask import make_response


class BaseController:
    @staticmethod
    def ToJson(obj):
        obj_dict = {attr: getattr(obj, attr) for attr in dir(obj) if
                    not attr.startswith("__") and not callable(getattr(obj, attr))}
        return json.dumps(obj_dict)

    @staticmethod
    def ReturnHttpNotAcceptable(obj):
        if isinstance(obj, str):
            return make_response(obj, 406)
        else:
            json_message = BaseController.ToJson(obj)
            return make_response(json_message, 406)
