"""Create address table

Revision ID: 872371389a84
Revises: 8c489e0db256
Create Date: 2018-03-02 21:33:08.125634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872371389a84'
down_revision = '8c489e0db256'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('openid', sa.String(128)),
        sa.Column('province', sa.String(1024)),
        sa.Column('city', sa.String(1024)),
        sa.Column('area', sa.String(1024)),
        sa.Column('address', sa.String(1024)),
        sa.Column('tel', sa.String(64)),
        sa.Column('name', sa.String(128))
    )


def downgrade():
    op.drop_table('address')
