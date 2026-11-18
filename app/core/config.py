from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Big Hangus API"
    debug: bool = False
    db_user: str = "admin"
    db_password: str = "secret"
    db_name: str = "big_hangus"
    db_host: str = "localhost"
    db_port: int = 5433
    database_url: str | None = None

    @property
    def db_url(self) -> str:
        if self.database_url:
            return self.database_url
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        ).render_as_string(hide_password=False)


config = Config()
