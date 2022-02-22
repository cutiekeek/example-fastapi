"""add user table

Revision ID: fd4a062eb2df
Revises: ef3504861933
Create Date: 2022-02-22 01:37:07.134613

"""
from ast import Str
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd4a062eb2df'
down_revision = 'ef3504861933'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
