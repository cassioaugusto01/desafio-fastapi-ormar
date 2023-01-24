from fastapi.testclient import TestClient
import ormar
import pytest
from models.usuario import Usuario
from tests.utils.usuarios import create_usuario_valido
import asyncio


def test_lista_todos_os_usuarios(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())

    response = client.get("/usuarios/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

def test_cria_usuario(client: TestClient) -> None:
    body = create_usuario_valido()
    response = client.post("/usuarios/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cpf"] == body["cpf"]

def test_obtem_um_usuario_por_id(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())
    # vai rodar o salvar e travar a execução nessa linha até terminar de rodas
    response = client.get(f"/usuarios/{usuario.id}")
    content = response.json()
    assert response.status_code == 200
    assert content["cpf"] == usuario.cpf

def test_obtem_usuario_inexistente_por_id(client: TestClient) -> None:
    response = client.get("/usuarios/1")
    content = response.json()
    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_update_usuario_existente(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())

    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/usuarios/{usuario.id}", json=atributos_para_atualizar)
    content = response.json()

    usuario_atualizado = loop.run_until_complete(Usuario.objects.get(id=usuario.id))

    assert response.status_code == 200
    assert content["nome"] == novo_nome
    assert usuario_atualizado.nome == novo_nome


def test_update_usuario_inexistente(client: TestClient) -> None:
    novo_nome = "Novo nome"
    atributos_para_atualizar = {"nome": novo_nome}

    response = client.patch(f"/usuarios/1", json=atributos_para_atualizar)
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_delete_usuario_existente(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())

    response = client.delete(f"/usuarios/{usuario.id}")

    with pytest.raises(ormar.exceptions.NoMatch):
        loop.run_until_complete(Usuario.objects.get(id=usuario.id))

    assert response.status_code == 200


def test_delete_usuario_inexistente(client: TestClient) -> None:
    response = client.delete(f"/usuarios/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"