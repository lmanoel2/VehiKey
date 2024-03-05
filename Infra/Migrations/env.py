from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from Domain.Entities.Base import Base

parentDirectory = os.path.dirname(os.getcwd())
entitiesDirectory = os.path.join(parentDirectory, "Domain", "Entities")

# Itera sobre os arquivos no diretório
for filename in os.listdir(entitiesDirectory):
    if filename.endswith('.py') and filename != '__init__.py':
        # Remove a extensão .py do nome do arquivo
        module_name = filename[:-3]
        # Importa dinamicamente o módulo
        module = importlib.import_module(f'Domain.Entities.{module_name}')

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
