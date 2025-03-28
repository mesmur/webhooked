"""add indexes

Revision ID: bf914e68143c
Revises: e95dcecf9c6a
Create Date: 2025-02-22 09:02:43.411010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf914e68143c'
down_revision: Union[str, None] = 'e95dcecf9c6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_webhooks_correlation_value'), 'webhooks', ['correlation_value'], unique=False)
    op.create_index(op.f('ix_webhooks_created_at'), 'webhooks', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_webhooks_created_at'), table_name='webhooks')
    op.drop_index(op.f('ix_webhooks_correlation_value'), table_name='webhooks')
    # ### end Alembic commands ###
