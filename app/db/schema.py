from datetime import date
from decimal import Decimal

from sqlalchemy import CheckConstraint, Date, MetaData, Numeric, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.core.config import config

engine = create_engine(config.db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)


class Ingrediente(Base):
    __tablename__ = "ingredientes"
    __table_args__ = (
        CheckConstraint("preco >= 0", name="preco"),
        CheckConstraint(
            "quantidade_disponivel >= 0",
            name="quantidade_disponivel",
        ),
        CheckConstraint(
            "quantidade_minima >= 0",
            name="quantidade_minima",
        ),
        CheckConstraint(
            "unidade_medida IN ('kg', 'litros')",
            name="unidade_medida",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    data_validade: Mapped[date | None] = mapped_column(Date, nullable=True)
    quantidade_disponivel: Mapped[Decimal] = mapped_column(
        Numeric(10, 3), nullable=False
    )
    unidade_medida: Mapped[str] = mapped_column(String(10), nullable=False)
    quantidade_minima: Mapped[Decimal] = mapped_column(Numeric(10, 3), nullable=False)
