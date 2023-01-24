from fastapi import APIRouter
import ormar
from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.post_controller import post_controller
from models.usuario import Usuario
from models.requests.patch_usuario import UsuarioUpdate
1
router = APIRouter()

@router.post("/")
@post_controller
async def add_item(entidade: Usuario):
    pass

@router.get("/")
@get_all_controller(Usuario)
async def list_item():
    pass

@router.get("/{id}")
@get_controller(Usuario)
async def get_usuario(id: int):
    pass

@router.patch("/{id}")
@patch_controller(Usuario)
async def patch_usuario(propriedades_atualizacao: UsuarioUpdate, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Usuario)
async def delete_usuario(id: int):
    pass