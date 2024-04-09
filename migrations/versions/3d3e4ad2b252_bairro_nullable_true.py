"""bairro nullable true

Revision ID: 3d3e4ad2b252
Revises: 52aa4c6aa9c2
Create Date: 2024-04-03 20:09:51.730092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d3e4ad2b252'
down_revision = '52aa4c6aa9c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('bairro',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('bairro',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###