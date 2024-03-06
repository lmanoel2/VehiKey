import os
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from alembic.config import Config
from alembic import command

def CreateOrCheckDatabase():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    alembic_config_path = os.path.join(current_dir, '..', '..', 'alembic.ini')

    alembic_cfg = Config(alembic_config_path)
    sqlalchemy_url = alembic_cfg.get_main_option("sqlalchemy.url")

    alembic_cfg.set_main_option("script_location", "Infra/Migrations")

    engine = create_engine(sqlalchemy_url)

    if not database_exists(engine.url):
        create_database(engine.url)

    command.upgrade(alembic_cfg, "head")