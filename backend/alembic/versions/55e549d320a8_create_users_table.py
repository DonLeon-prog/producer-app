"""create users table

Revision ID: 55e549d320a8
Revises:
Create Date: 2026-05-01 15:48:47.553372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '55e549d320a8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('telegram_id', sa.String(), nullable=False, unique=True),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('user_type', sa.String(), nullable=True),
        sa.Column('profile', postgresql.JSONB(), nullable=True),
        sa.Column('plan', sa.String(), nullable=False, server_default='free'),
        sa.Column('requests_today', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('last_request_date', sa.Date(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("plan IN ('free', 'pro', 'producer')", name='ck_users_plan'),
    )
    op.create_index('ix_users_telegram_id', 'users', ['telegram_id'], unique=True)


def downgrade() -> None:
    op.drop_index('ix_users_telegram_id', table_name='users')
    op.drop_table('users')
