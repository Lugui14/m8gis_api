"""alter numero column

Revision ID: 7a0bfeb125fa
Revises: f33bc0632770
Create Date: 2024-04-01 21:48:20.630504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a0bfeb125fa'
down_revision = 'f33bc0632770'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
