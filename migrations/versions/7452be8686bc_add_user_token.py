"""add user.token

Revision ID: 7452be8686bc
Revises: b67a68c1110b
Create Date: 2017-03-14 18:08:31.749171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7452be8686bc'
down_revision = 'b67a68c1110b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=128), nullable=True))
    op.create_unique_constraint(None, 'user', ['token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
