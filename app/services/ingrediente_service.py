from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.schema import Ingrediente
from app.models.ingrediente import IngredienteCreate, IngredienteUpdate


class IngredienteNaoEncontrado(Exception):
    pass


class NomeIngredienteDuplicado(Exception):
    pass


class IngredienteService:
    def __init__(self, session: Session):
        self._db = session

    def listar(
        self,
        nome: str | None = None,
        em_baixa: bool | None = None,
    ) -> list[Ingrediente]:
        query = self._db.query(Ingrediente)
        if nome:
            query = query.filter(Ingrediente.nome.ilike(f"%{nome}%"))
        if em_baixa:
            query = query.filter(
                Ingrediente.quantidade_disponivel < Ingrediente.quantidade_minima
            )
        return query.order_by(Ingrediente.id).all()

    def buscar(self, ingrediente_id: int) -> Ingrediente | None:
        return self._db.get(Ingrediente, ingrediente_id)

    def criar(self, dados: IngredienteCreate) -> Ingrediente:
        ingrediente = Ingrediente(**self._dados_do_modelo(dados))
        self._db.add(ingrediente)
        self._commit_ou_duplicado()
        self._db.refresh(ingrediente)
        return ingrediente

    def atualizar(
        self,
        ingrediente_id: int,
        dados: IngredienteUpdate,
    ) -> Ingrediente:
        ingrediente = self.buscar(ingrediente_id)
        if ingrediente is None:
            raise IngredienteNaoEncontrado

        for campo, valor in self._dados_do_modelo(dados).items():
            setattr(ingrediente, campo, valor)

        self._commit_ou_duplicado()
        self._db.refresh(ingrediente)
        return ingrediente

    def excluir(self, ingrediente_id: int) -> None:
        ingrediente = self.buscar(ingrediente_id)
        if ingrediente is None:
            raise IngredienteNaoEncontrado

        self._db.delete(ingrediente)
        self._db.commit()

    def _dados_do_modelo(
        self,
        dados: IngredienteCreate | IngredienteUpdate,
    ) -> dict[str, object]:
        valores = dados.model_dump()
        valores["unidade_medida"] = dados.unidade_medida.value
        return valores

    def _commit_ou_duplicado(self) -> None:
        try:
            self._db.commit()
        except IntegrityError:
            self._db.rollback()
            raise NomeIngredienteDuplicado from None
