import databases
import sqlalchemy
import os
from fastapi import FastAPI

def get_db_uri(*, user, password, host, db):
    return f'postgresql://{user}:{password}@{host}:5432/{db}'

#TODO: Refatorar para usar variaveis de ambiente

DATABASE_URL = get_db_uri(
    user='postgres',
    password='qwerty123456',
    host='localhost',
    db="desafio_cadhab",
)

if os.environ.get("TEST_DATABASE") == "true":
    DATABASE_URL = 'sqlite:///testedb.sqlite'

TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()

def setup_database(app: FastAPI):
    app.state.database = database

    @app.on_event("startup")
    async def startup() -> None:
        database_ = app.state.database
        if not database_.is_connected:
            await database_.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        database_ = app.state.database
        if database_.is_connected:
            await database_.disconnect()