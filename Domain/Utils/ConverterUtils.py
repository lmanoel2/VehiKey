import json

def ParseClassToJson(obj):
    obj_dict = ParseClassToDict(obj)
    return json.dumps(obj_dict)

def ParseClassToDict(obj):
    return {attr: getattr(obj, attr) for attr in dir(obj) if
            not attr.startswith("__") and not callable(getattr(obj, attr))}