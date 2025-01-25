"""create_genres_table

Revision ID: 5060505f1704
Revises: a32b92c7680d
Create Date: 2025-01-25 14:06:35.798734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5060505f1704'
down_revision: Union[str, None] = 'a32b92c7680d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'genres',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),

        sa.UniqueConstraint('name', name='unq_genres_name'),
    )



def downgrade() -> None:
    op.drop_table('genres')
