"""create_seats_table

Revision ID: 2ef21905a129
Revises: 8fabe86c6a77
Create Date: 2025-01-25 14:20:23.578328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import SMALLINT, DECIMAL

# revision identifiers, used by Alembic.
revision: str = '2ef21905a129'
down_revision: Union[str, None] = '8fabe86c6a77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'seats',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('theater_id', sa.Integer(), nullable=False),
        sa.Column('row', sa.String(5), nullable=False),
        sa.Column('number', SMALLINT(unsigned=True), nullable=False),
        sa.Column('price', DECIMAL(10, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(['theater_id'], ['theaters.id'], ondelete='CASCADE', name='fk_seats_theater_id'),
        sa.UniqueConstraint('theater_id', 'row', 'number', name='unq_seats_theater_id_row_number'),
        sa.CheckConstraint('price > 0', name='chk_seats_price_positive'),
    )


def downgrade() -> None:
    op.drop_constraint('fk_seats_theater_id', table_name='seats', type_='foreignkey')
    op.drop_constraint('chk_seats_price_positive', table_name='seats', type_='check')
    op.drop_index('unq_seats_theater_id_row_number', table_name='seats')
    op.drop_table('seats')
