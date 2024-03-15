import json
import inspect

def ParseClassToJson(obj):
    obj_dict = ParseClassToDict(obj)
    return json.dumps(obj_dict)

def ParseObjectToClass(source, destClass):
    dest = destClass()
    for attr_name in dir(source):
        if not attr_name.startswith("__") and hasattr(dest, attr_name):
            setattr(dest, attr_name, getattr(source, attr_name))
    return dest

def ParseModelToResponseView(source, destClass):
    constructorParams = inspect.signature(destClass.__init__).parameters
    attributes = {param: getattr(source, param, None) for param in constructorParams if param != 'self'}
    destinationInstance = destClass(**attributes)
    return destinationInstance

def ParseClassToDict(obj):
    return {attr: getattr(obj, attr) for attr in dir(obj) if
            not attr.startswith("__") and not callable(getattr(obj, attr))}