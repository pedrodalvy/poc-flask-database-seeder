"""create_showtimes_table

Revision ID: 254f94106e6a
Revises: 2ef21905a129
Create Date: 2025-01-25 14:31:34.446523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '254f94106e6a'
down_revision: Union[str, None] = '2ef21905a129'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'showtimes',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('movie_id', sa.Integer(), nullable=False),
        sa.Column('theater_id', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('end_time', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['theater_id'], ['theaters.id'], ondelete='CASCADE'),
        sa.UniqueConstraint('movie_id', 'theater_id', 'start_time', name='unq_showtimes_movie_id_theater_id_start_time'),
        sa.CheckConstraint('end_time > start_time', name='chk_showtimes_end_time_after_start_time'),

        sa.Index('idx_showtimes_movie_id', 'movie_id'),
    )


def downgrade() -> None:
    op.drop_table('showtimes')
