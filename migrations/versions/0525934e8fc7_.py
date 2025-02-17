"""empty message

Revision ID: 0525934e8fc7
Revises: db056d214bf9
Create Date: 2025-02-15 13:43:59.586842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0525934e8fc7'
down_revision = 'db056d214bf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
