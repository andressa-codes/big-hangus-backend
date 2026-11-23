# Big Hangus Backend

Backend do sistema de estoque da Big Hangus. Disponibiliza uma API REST para o CRUD de ingredientes do estoque, permitindo cadastrar, consultar, listar, alterar e excluir ingredientes, além de identificar itens em baixa.

## Tecnologias

- **Python** — linguagem do projeto
- **FastAPI** — framework da API REST
- **Docker** — containerização da aplicação e do banco
- **PostgreSQL** — banco de dados relacional

## Repositórios relacionados

- Frontend: https://github.com/vanescaSnt/big-hangus-frontend

## Documentação

- [Documento de visão](docs/doc-visao.md)
- [Documento de modelos](docs/doc-modelos.md)
- [Backlog](docs/backlog.md)

## Setup

Instale o uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Crie o `.env` e suba o PostgreSQL:

```bash
cp .env.example .env
docker compose up -d db
```

Instale as dependências, aplique as migrations e inicie o servidor:

```bash
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

O container do PostgreSQL usa a porta `5433` no host (definida por `DB_PORT`), evitando conflito com um PostgreSQL local na `5432`.

API: http://localhost:8000 — Docs: http://localhost:8000/docs

## Docker

```bash
docker compose up --build
```

O serviço `migrate` roda `alembic upgrade head` antes do `web` iniciar.

## Migrations

O schema é gerenciado pelo Alembic (`app.main` não cria tabelas). As migrations ficam em `app/db/migrations/versions` e são versionadas.

```bash
# aplicar
uv run alembic upgrade head

# criar após alterar os models
uv run alembic revision --autogenerate -m "descrição da mudança"

# reverter a última
uv run alembic downgrade -1
```

Revise o arquivo gerado antes de aplicar. Nunca edite uma migration já aplicada em ambiente compartilhado; crie uma nova. Em produção, rode `alembic upgrade head` como etapa de deploy, não no entrypoint da aplicação.

## Testes

Os testes usam SQLite em memória e aplicam todas as migrations, sem precisar de Docker/PostgreSQL:

```bash
uv run pytest
```

Para usar outro banco, defina `TEST_DATABASE_URL`. Recursos específicos do PostgreSQL devem ser validados também nele.

