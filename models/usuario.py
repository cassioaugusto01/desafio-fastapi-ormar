import ormar
import re
from pydantic import validator
from sqlalchemy.sql.expression import table
from config import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    cpf: str = ormar.String(max_length=20)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    telefone: str = ormar.String(max_length=20)