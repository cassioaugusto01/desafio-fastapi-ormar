from functools import wraps
import ormar
from pydantic import BaseModel

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada

def post_controller (func):
    @wraps(func)
    async def wrapper(entidade: ormar.Model):
        await entidade.save()
        return entidade
    return wrapper