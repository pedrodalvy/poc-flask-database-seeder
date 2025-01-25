"""create_reservations_table

Revision ID: d8c799019f8c
Revises: 254f94106e6a
Create Date: 2025-01-25 14:38:15.520126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8c799019f8c'
down_revision: Union[str, None] = '254f94106e6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'reservations',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('showtime_id', sa.Integer(), nullable=False),
        sa.Column('seat_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('reservation_time', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('status', sa.Enum('confirmed', 'cancelled', name='reservation_status'), nullable=False),

        sa.ForeignKeyConstraint(['showtime_id'], ['showtimes.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['seat_id'], ['seats.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.UniqueConstraint('showtime_id', 'seat_id', name='unq_reservations_showtime_id_seat_id'),

        sa.Index('idx_reservations_user_id', 'user_id'),
    )


def downgrade() -> None:
    op.drop_table('reservations')
