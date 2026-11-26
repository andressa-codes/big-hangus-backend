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


@router.get(
    "/ingredientes",
    response_model=list[IngredienteResponse],
    summary="Listar ingredientes",
    description=(
        "Lista os ingredientes do estoque. Filtros opcionais: `nome` (busca por "
        "trecho do nome) e `em_baixa=true` (apenas os ingredientes com quantidade "
        "disponível abaixo da mínima)."
    ),
)
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
    summary="Criar ingrediente",
    description="Cadastra um ingrediente no estoque. O nome deve ser único.",
    responses={
        409: {"description": "Já existe um ingrediente com esse nome"},
        422: {"description": "Dados inválidos (valor negativo, unidade inválida...)"},
    },
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


@router.get(
    "/ingredientes/{ingrediente_id}",
    response_model=IngredienteResponse,
    summary="Buscar ingrediente",
    description="Retorna os dados completos de um ingrediente pelo identificador.",
    responses={404: {"description": "Ingrediente não encontrado"}},
)
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


@router.put(
    "/ingredientes/{ingrediente_id}",
    response_model=IngredienteResponse,
    summary="Atualizar ingrediente",
    description="Altera os dados de um ingrediente. O nome deve continuar único.",
    responses={
        404: {"description": "Ingrediente não encontrado"},
        409: {"description": "Já existe outro ingrediente com esse nome"},
        422: {"description": "Dados inválidos (valor negativo, unidade inválida...)"},
    },
)
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
    summary="Excluir ingrediente",
    description="Remove um ingrediente do estoque. Não retorna conteúdo.",
    responses={404: {"description": "Ingrediente não encontrado"}},
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