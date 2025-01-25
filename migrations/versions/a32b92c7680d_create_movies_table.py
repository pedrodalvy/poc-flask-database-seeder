"""create_movies_table

Revision ID: a32b92c7680d
Revises: 00b80a547245
Create Date: 2025-01-25 13:54:04.852224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import SMALLINT

# revision identifiers, used by Alembic.
revision: str = 'a32b92c7680d'
down_revision: Union[str, None] = '00b80a547245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('poster_url', sa.String(512), nullable=False),
        sa.Column('duration_minutes', SMALLINT(unsigned=True), nullable=False),
        sa.Column('release_date', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.Index('idx_movies_title', 'title', unique=False),
    )


def downgrade() -> None:
    op.drop_table('movies')
