from typing import List, Optional
from pydantic import BaseModel

class UsuarioUpdate(BaseModel):
    cpf: Optional[str]
    nome: Optional[str]
    email: Optional[str]
    telefone: Optional[str]