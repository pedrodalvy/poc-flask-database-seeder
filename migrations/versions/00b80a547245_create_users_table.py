"""create_users_table

Revision ID: 00b80a547245
Revises: 
Create Date: 2025-01-25 12:35:33.041641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '00b80a547245'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('role', sa.Enum('user', 'admin', name='role'), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=True),

        sa.UniqueConstraint('email', name='unq_users_email'),
    )


def downgrade() -> None:
    op.drop_table('users')
