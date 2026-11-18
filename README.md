# Big Hangus Backend

Backend built with Python 3.13, FastAPI, SQLAlchemy, PostgreSQL and uv.

## Setup

Install uv (if not installed):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create the environment file and start PostgreSQL:

```bash
cp .env.example .env
docker compose up -d db
```

Install dependencies, apply the migrations and start the server:

```bash
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

The PostgreSQL container is published on host port `5433` by default (set by
`DB_PORT`), so it does not conflict with a local PostgreSQL on `5432`.

The API is available at http://localhost:8000 and the docs at
http://localhost:8000/docs.

## Running with Docker

```bash
docker compose up --build
```

The `migrate` service runs `alembic upgrade head` and the `web` service only
starts after it completes successfully.

## Migrations

The schema is managed by Alembic; `app.main` does not create tables on startup.
Migrations live in `app/db/migrations/versions` and are committed to the
repository.

Apply the latest migrations (after pulling changes or deploying):

```bash
uv run alembic upgrade head
```

Create a migration after changing the models:

```bash
uv run alembic revision --autogenerate -m "describe the change"
```

Review the generated file in `app/db/migrations/versions` before applying it.
Never edit a migration that has already been applied in a shared environment;
create a new one instead.

Roll back the last migration:

```bash
uv run alembic downgrade -1
```

In production, run `alembic upgrade head` as a deploy step (before starting the
new version), not in the application entrypoint.

## Tests

Tests use an in-memory SQLite database and apply all Alembic migrations before
running, so Docker/PostgreSQL is not required:

```bash
uv run pytest
```

To run the tests against another database, set `TEST_DATABASE_URL` (for example,
a PostgreSQL test database). Keep in mind that migrations with
PostgreSQL-specific features must also be validated against PostgreSQL.

## Example requests

1. Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "Ada Lovelace"}'
```

2. Get All Users

```bash
curl -X GET "http://localhost:8000/api/v1/users"
```

3. Get a User by ID (replace `1` with the actual ID)

```bash
curl -X GET "http://localhost:8000/api/v1/users/1"
```

4. Update a User

```bash
curl -X PUT "http://localhost:8000/api/v1/users/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Grace Hopper"}'
```

5. Delete a User

```bash
curl -X DELETE "http://localhost:8000/api/v1/users/1"
```
