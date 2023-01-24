from tests.utils.usuarios import create_usuario_valido
from models.usuario import Usuario
import pytest

def test_cria_usuario_valido() -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)