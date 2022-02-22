"""add foreign key to posts table

Revision ID: 220968be63d9
Revises: fd4a062eb2df
Create Date: 2022-02-22 01:47:49.360231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '220968be63d9'
down_revision = 'fd4a062eb2df'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
