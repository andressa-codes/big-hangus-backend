from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, computed_field


class UnidadeMedida(str, Enum):
    KG = "kg"
    LITROS = "litros"


class IngredienteBase(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    data_validade: date | None = None
    quantidade_disponivel: Decimal = Field(ge=0, max_digits=10, decimal_places=3)
    unidade_medida: UnidadeMedida
    quantidade_minima: Decimal = Field(ge=0, max_digits=10, decimal_places=3)


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteUpdate(IngredienteBase):
    pass


class IngredienteResponse(IngredienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

    @computed_field
    @property
    def em_baixa(self) -> bool:
        return self.quantidade_disponivel < self.quantidade_minima
