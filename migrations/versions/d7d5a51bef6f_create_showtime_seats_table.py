"""create_showtime_seats_table

Revision ID: d7d5a51bef6f
Revises: d8c799019f8c
Create Date: 2025-01-25 14:46:01.770912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import DECIMAL

# revision identifiers, used by Alembic.
revision: str = 'd7d5a51bef6f'
down_revision: Union[str, None] = 'd8c799019f8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'showtime_seats',
        sa.Column('showtime_id', sa.Integer(), nullable=False),
        sa.Column('seat_id', sa.Integer(), nullable=False),
        sa.Column('reservation_id', sa.Integer(), nullable=True),
        sa.Column('status', sa.Enum('available', 'reserved', 'cancelled', name='showtime_seat_status'), nullable=False),
        sa.Column('price', DECIMAL(10, 2), nullable=False),

        sa.ForeignKeyConstraint(['showtime_id'], ['showtimes.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['seat_id'], ['seats.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('showtime_id', 'seat_id'),
        sa.CheckConstraint('price > 0', name='chk_showtime_seats_price_positive'),
    )


def downgrade() -> None:
    op.drop_table('showtime_seats')
