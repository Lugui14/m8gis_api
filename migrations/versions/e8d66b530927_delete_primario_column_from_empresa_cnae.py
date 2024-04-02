"""delete primario column from empresa_cnae

Revision ID: e8d66b530927
Revises: 746a3f4a814d
Create Date: 2024-04-02 19:56:04.793289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8d66b530927'
down_revision = '746a3f4a814d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresa_cnae', schema=None) as batch_op:
        batch_op.drop_column('primario')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresa_cnae', schema=None) as batch_op:
        batch_op.add_column(sa.Column('primario', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
