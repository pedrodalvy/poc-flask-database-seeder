"""create_genres_movies_table

Revision ID: a17910534a84
Revises: 5060505f1704
Create Date: 2025-01-25 14:11:19.554771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a17910534a84'
down_revision: Union[str, None] = '5060505f1704'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'genres_movies',
        sa.Column('genre_id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('genre_id', 'movie_id'),
    )


def downgrade() -> None:
    op.drop_table('genres_movies')
