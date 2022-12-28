"""empty message
Revision ID: 10001
Revises: 1001
Create Date: 2022-12-28 16:30:20.119025
"""

# revision identifiers, used by Alembic.
revision = '10001'
down_revision = '1001'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    ### end Alembic commands ###
