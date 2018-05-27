"""add column age

Revision ID: d95b21ff9dee
Revises: 6872eb55fafe
Create Date: 2018-05-27 15:06:05.376312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95b21ff9dee'
down_revision = '6872eb55fafe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'age')
    # ### end Alembic commands ###