"""which recived comments are new

Revision ID: 25a79e570369
Revises: b99c5ba9f48b
Create Date: 2021-02-19 22:21:32.950765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25a79e570369'
down_revision = 'b99c5ba9f48b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_recived_comments_read_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('last_recived_comments_read_time')

    # ### end Alembic commands ###
