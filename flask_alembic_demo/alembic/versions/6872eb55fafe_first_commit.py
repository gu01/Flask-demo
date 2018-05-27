"""first commit

Revision ID: 6872eb55fafe
Revises: 
Create Date: 2018-05-27 15:02:55.444448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6872eb55fafe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
