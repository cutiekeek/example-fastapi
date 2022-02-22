"""add content column to post table

Revision ID: ef3504861933
Revises: 27f88af3aacc
Create Date: 2022-02-22 01:32:44.718599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef3504861933'
down_revision = '27f88af3aacc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
