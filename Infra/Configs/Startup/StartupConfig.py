import os
import importlib
from flask import Blueprint


def RegisterBlueprints(app):
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    previous_dir = os.path.dirname(parent_dir)
    previous_dir = os.path.dirname(previous_dir)
    controllers_dir = os.path.join(previous_dir, 'controllers')
    for filename in os.listdir(controllers_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"Infra.Controllers.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for item_name in dir(module):
                item = getattr(module, item_name)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)