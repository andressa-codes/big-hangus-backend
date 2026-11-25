from collections.abc import Iterator

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.db.schema import SessionLocal
from app.models.ingrediente import (
    IngredienteCreate,
    IngredienteResponse,
    IngredienteUpdate,
)
from app.services.ingrediente_service import (
    IngredienteNaoEncontrado,
    IngredienteService,
    NomeIngredienteDuplicado,
)

router = APIRouter()


def get_ingrediente_service() -> Iterator[IngredienteService]:
    session = SessionLocal()
    try:
        yield IngredienteService(session=session)
    finally:
        session.close()


@router.get("/ingredientes", response_model=list[IngredienteResponse])
def listar_ingredientes(
    nome: str | None = None,
    em_baixa: bool | None = None,
    service: IngredienteService = Depends(get_ingrediente_service),
):
    return service.listar(nome=nome, em_baixa=em_baixa)


@router.post(
    "/ingredientes",
    response_model=IngredienteResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_ingrediente(
    ingrediente: IngredienteCreate,
    service: IngredienteService = Depends(get_ingrediente_service),
):
    try:
        return service.criar(ingrediente)
    except NomeIngredienteDuplicado:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um ingrediente com esse nome",
        ) from None


@router.get("/ingredientes/{ingrediente_id}", response_model=IngredienteResponse)
def buscar_ingrediente(
    ingrediente_id: int,
    service: IngredienteService = Depends(get_ingrediente_service),
):
    ingrediente = service.buscar(ingrediente_id)
    if ingrediente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingrediente não encontrado",
        )
    return ingrediente


@router.put("/ingredientes/{ingrediente_id}", response_model=IngredienteResponse)
def atualizar_ingrediente(
    ingrediente_id: int,
    ingrediente: IngredienteUpdate,
    service: IngredienteService = Depends(get_ingrediente_service),
):
    try:
        return service.atualizar(ingrediente_id, ingrediente)
    except IngredienteNaoEncontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingrediente não encontrado",
        ) from None
    except NomeIngredienteDuplicado:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um ingrediente com esse nome",
        ) from None


@router.delete(
    "/ingredientes/{ingrediente_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def excluir_ingrediente(
    ingrediente_id: int,
    service: IngredienteService = Depends(get_ingrediente_service),
) -> Response:
    try:
        service.excluir(ingrediente_id)
    except IngredienteNaoEncontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingrediente não encontrado",
        ) from None
    return Response(status_code=status.HTTP_204_NO_CONTENT)
