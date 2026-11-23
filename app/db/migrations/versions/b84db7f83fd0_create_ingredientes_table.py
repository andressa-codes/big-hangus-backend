"""create ingredientes table

Revision ID: b84db7f83fd0
Revises: 1f43ce7adc1b
Create Date: 2026-11-23 16:09:22.686926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b84db7f83fd0'
down_revision: Union[str, Sequence[str], None] = '1f43ce7adc1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "ingredientes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("preco", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("data_validade", sa.Date(), nullable=True),
        sa.Column(
            "quantidade_disponivel",
            sa.Numeric(precision=10, scale=3),
            nullable=False,
        ),
        sa.Column("unidade_medida", sa.String(length=10), nullable=False),
        sa.Column(
            "quantidade_minima",
            sa.Numeric(precision=10, scale=3),
            nullable=False,
        ),
        sa.CheckConstraint("preco >= 0", name="preco"),
        sa.CheckConstraint(
            "quantidade_disponivel >= 0",
            name="quantidade_disponivel",
        ),
        sa.CheckConstraint(
            "quantidade_minima >= 0",
            name="quantidade_minima",
        ),
        sa.CheckConstraint(
            "unidade_medida IN ('kg', 'litros')",
            name="unidade_medida",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ingredientes")),
        sa.UniqueConstraint("nome", name=op.f("uq_ingredientes_nome")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("ingredientes")
