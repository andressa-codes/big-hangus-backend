from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, computed_field


class UnidadeMedida(str, Enum):
    KG = "kg"
    LITROS = "litros"


# exemplo exibido na documentação (/docs)
EXEMPLO_INGREDIENTE = {
    "nome": "Queijo mussarela",
    "preco": 42.90,
    "data_validade": "2026-12-20",
    "quantidade_disponivel": 8.5,
    "unidade_medida": "kg",
    "quantidade_minima": 2,
}


class IngredienteBase(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    data_validade: date | None = None
    quantidade_disponivel: Decimal = Field(ge=0, max_digits=10, decimal_places=3)
    unidade_medida: UnidadeMedida
    quantidade_minima: Decimal = Field(ge=0, max_digits=10, decimal_places=3)


class IngredienteCreate(IngredienteBase):
    model_config = ConfigDict(json_schema_extra={"examples": [EXEMPLO_INGREDIENTE]})


class IngredienteUpdate(IngredienteBase):
    model_config = ConfigDict(json_schema_extra={"examples": [EXEMPLO_INGREDIENTE]})


class IngredienteResponse(IngredienteBase):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [{"id": 1, **EXEMPLO_INGREDIENTE, "em_baixa": False}]
        },
    )

    id: int

    @computed_field
    @property
    def em_baixa(self) -> bool:
        return self.quantidade_disponivel < self.quantidade_minima