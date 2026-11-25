from typing import Any

import pytest
from fastapi.testclient import TestClient

from app.api.v1.ingrediente import get_ingrediente_service
from app.db.schema import Ingrediente
from app.main import app
from app.services.ingrediente_service import IngredienteService
from tests.test_db import TestingSessionLocal

client = TestClient(app)


def override_get_ingrediente_service():
    session = TestingSessionLocal()
    try:
        yield IngredienteService(session=session)
    finally:
        session.close()


app.dependency_overrides[get_ingrediente_service] = override_get_ingrediente_service


@pytest.fixture(autouse=True)
def limpar_ingredientes():
    session = TestingSessionLocal()
    session.query(Ingrediente).delete()
    session.commit()
    session.close()
    yield


def dados_ingrediente(**sobrescritas: Any) -> dict[str, Any]:
    dados: dict[str, Any] = {
        "nome": "Queijo mussarela",
        "preco": "42.90",
        "data_validade": "2026-12-20",
        "quantidade_disponivel": "8.5",
        "unidade_medida": "kg",
        "quantidade_minima": "2",
    }
    dados.update(sobrescritas)
    return dados


def criar_ingrediente(**sobrescritas: Any) -> dict[str, Any]:
    resposta = client.post(
        "/api/v1/ingredientes",
        json=dados_ingrediente(**sobrescritas),
    )
    assert resposta.status_code == 201
    return resposta.json()


def test_cria_ingrediente() -> None:
    resposta = client.post(
        "/api/v1/ingredientes",
        json=dados_ingrediente(),
    )

    assert resposta.status_code == 201
    ingrediente = resposta.json()
    assert ingrediente["nome"] == "Queijo mussarela"
    assert ingrediente["unidade_medida"] == "kg"
    assert ingrediente["em_baixa"] is False


def test_cria_ingrediente_em_baixa() -> None:
    ingrediente = criar_ingrediente(quantidade_disponivel="1")

    assert ingrediente["em_baixa"] is True


def test_cria_ingrediente_com_nome_duplicado() -> None:
    criar_ingrediente()

    resposta = client.post(
        "/api/v1/ingredientes",
        json=dados_ingrediente(),
    )

    assert resposta.status_code == 409
    assert resposta.json()["detail"] == "Já existe um ingrediente com esse nome"


@pytest.mark.parametrize(
    "campo",
    ["preco", "quantidade_disponivel", "quantidade_minima"],
)
def test_cria_ingrediente_com_valor_negativo(campo: str) -> None:
    resposta = client.post(
        "/api/v1/ingredientes",
        json=dados_ingrediente(**{campo: "-1"}),
    )

    assert resposta.status_code == 422


def test_cria_ingrediente_com_unidade_invalida() -> None:
    resposta = client.post(
        "/api/v1/ingredientes",
        json=dados_ingrediente(unidade_medida="unidade"),
    )

    assert resposta.status_code == 422


def test_lista_ingredientes_vazia() -> None:
    resposta = client.get("/api/v1/ingredientes")

    assert resposta.status_code == 200
    assert resposta.json() == []


def test_lista_ingredientes() -> None:
    criar_ingrediente(nome="Queijo mussarela")
    criar_ingrediente(nome="Presunto")

    resposta = client.get("/api/v1/ingredientes")

    assert resposta.status_code == 200
    nomes = [item["nome"] for item in resposta.json()]
    assert nomes == ["Queijo mussarela", "Presunto"]


def test_filtra_ingredientes_por_nome() -> None:
    criar_ingrediente(nome="Queijo mussarela")
    criar_ingrediente(nome="Presunto")

    resposta = client.get(
        "/api/v1/ingredientes",
        params={"nome": "MUSSARELA"},
    )

    assert resposta.status_code == 200
    nomes = [item["nome"] for item in resposta.json()]
    assert nomes == ["Queijo mussarela"]


def test_filtra_ingredientes_em_baixa() -> None:
    criar_ingrediente(nome="Queijo mussarela", quantidade_disponivel="1")
    criar_ingrediente(nome="Presunto", quantidade_disponivel="10")

    resposta = client.get(
        "/api/v1/ingredientes",
        params={"em_baixa": "true"},
    )

    assert resposta.status_code == 200
    nomes = [item["nome"] for item in resposta.json()]
    assert nomes == ["Queijo mussarela"]


def test_busca_ingrediente_por_id() -> None:
    criado = criar_ingrediente()

    resposta = client.get(f"/api/v1/ingredientes/{criado['id']}")

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Queijo mussarela"


def test_busca_ingrediente_inexistente() -> None:
    resposta = client.get("/api/v1/ingredientes/999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Ingrediente não encontrado"


def test_atualiza_ingrediente() -> None:
    criado = criar_ingrediente()

    resposta = client.put(
        f"/api/v1/ingredientes/{criado['id']}",
        json=dados_ingrediente(nome="Queijo prato", quantidade_disponivel="1"),
    )

    assert resposta.status_code == 200
    ingrediente = resposta.json()
    assert ingrediente["nome"] == "Queijo prato"
    assert ingrediente["em_baixa"] is True


def test_atualiza_ingrediente_inexistente() -> None:
    resposta = client.put(
        "/api/v1/ingredientes/999",
        json=dados_ingrediente(),
    )

    assert resposta.status_code == 404


def test_atualiza_ingrediente_com_nome_duplicado() -> None:
    criar_ingrediente(nome="Queijo mussarela")
    outro = criar_ingrediente(nome="Presunto")

    resposta = client.put(
        f"/api/v1/ingredientes/{outro['id']}",
        json=dados_ingrediente(nome="Queijo mussarela"),
    )

    assert resposta.status_code == 409


def test_atualiza_ingrediente_com_dados_invalidos() -> None:
    criado = criar_ingrediente()

    resposta = client.put(
        f"/api/v1/ingredientes/{criado['id']}",
        json=dados_ingrediente(preco="-1"),
    )

    assert resposta.status_code == 422


def test_exclui_ingrediente() -> None:
    criado = criar_ingrediente()

    resposta = client.delete(f"/api/v1/ingredientes/{criado['id']}")

    assert resposta.status_code == 204
    assert client.get(f"/api/v1/ingredientes/{criado['id']}").status_code == 404
    assert client.get("/api/v1/ingredientes").json() == []


def test_exclui_ingrediente_inexistente() -> None:
    resposta = client.delete("/api/v1/ingredientes/999")

    assert resposta.status_code == 404
