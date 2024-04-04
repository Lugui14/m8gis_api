"""increase char limits

Revision ID: 359869a5200f
Revises: 3d3e4ad2b252
Create Date: 2024-04-03 20:28:33.230132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359869a5200f'
down_revision = '3d3e4ad2b252'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('socio', schema=None) as batch_op:
        batch_op.alter_column('nome_socio',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('nome_representante_legal',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('socio', schema=None) as batch_op:
        batch_op.alter_column('nome_representante_legal',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('nome_socio',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
