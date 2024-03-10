import json

def ParseClassToJson(obj):
    obj_dict = {attr: getattr(obj, attr) for attr in dir(obj) if
                not attr.startswith("__") and not callable(getattr(obj, attr))}
    return json.dumps(obj_dict)
