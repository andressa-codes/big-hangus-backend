from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.models.ingrediente import (
    IngredienteCreate,
    IngredienteResponse,
    UnidadeMedida,
)


def ingrediente_data(**overrides: object) -> dict[str, object]:
    data: dict[str, object] = {
        "nome": "Queijo mussarela",
        "preco": Decimal("42.90"),
        "data_validade": "2026-12-20",
        "quantidade_disponivel": Decimal("8.5"),
        "unidade_medida": "kg",
        "quantidade_minima": Decimal("2"),
    }
    data.update(overrides)
    return data


def test_cria_ingrediente_valido() -> None:
    ingrediente = IngredienteCreate(**ingrediente_data())

    assert ingrediente.nome == "Queijo mussarela"
    assert ingrediente.unidade_medida is UnidadeMedida.KG


@pytest.mark.parametrize(
    "campo",
    ["preco", "quantidade_disponivel", "quantidade_minima"],
)
def test_rejeita_valores_negativos(campo: str) -> None:
    with pytest.raises(ValidationError):
        IngredienteCreate(**ingrediente_data(**{campo: Decimal("-1")}))


def test_rejeita_unidade_invalida() -> None:
    with pytest.raises(ValidationError):
        IngredienteCreate(**ingrediente_data(unidade_medida="unidade"))


@pytest.mark.parametrize(
    ("quantidade_disponivel", "quantidade_minima", "esperado"),
    [
        (Decimal("1"), Decimal("2"), True),
        (Decimal("2"), Decimal("2"), False),
        (Decimal("3"), Decimal("2"), False),
    ],
)
def test_calcula_em_baixa(
    quantidade_disponivel: Decimal,
    quantidade_minima: Decimal,
    esperado: bool,
) -> None:
    ingrediente = IngredienteResponse(
        id=1,
        **ingrediente_data(
            quantidade_disponivel=quantidade_disponivel,
            quantidade_minima=quantidade_minima,
        ),
    )

    assert ingrediente.em_baixa is esperado
    assert ingrediente.model_dump()["em_baixa"] is esperado
