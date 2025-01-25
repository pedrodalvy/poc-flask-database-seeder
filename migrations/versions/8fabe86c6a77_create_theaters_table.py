"""create_theaters_table

Revision ID: 8fabe86c6a77
Revises: a17910534a84
Create Date: 2025-01-25 14:16:57.534536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fabe86c6a77'
down_revision: Union[str, None] = 'a17910534a84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'theaters',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('location', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.Index('idx_theaters_name', 'name', unique=False)
    )



def downgrade() -> None:
    op.drop_index('idx_theaters_name', table_name='theaters')
    op.drop_table('theaters')
