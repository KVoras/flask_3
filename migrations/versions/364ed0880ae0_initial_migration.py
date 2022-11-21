"""Initial migration.

Revision ID: 364ed0880ae0
Revises: 
Create Date: 2022-11-21 20:17:30.186361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364ed0880ae0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.drop_column('address')

    # ### end Alembic commands ###