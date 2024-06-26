"""endereco unique constraint multiple columns

Revision ID: 3864ddeede13
Revises: e65ae9ec824f
Create Date: 2024-05-17 17:20:58.986702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3864ddeede13'
down_revision = 'e65ae9ec824f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['logradouro', 'numero', 'bairro', 'tipo_logradouro', 'cep', 'municipio_id', 'complemento'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
