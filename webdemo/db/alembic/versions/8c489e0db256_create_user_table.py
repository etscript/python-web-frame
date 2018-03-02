"""Create user table

Revision ID: 8c489e0db256
Revises: 
Create Date: 2018-03-02 15:04:03.940900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c489e0db256'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('openid', sa.String(255), nullable=False),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('gender', sa.String(64)),
        sa.Column('country', sa.Integer),
        sa.Column('province', sa.String(255)),
        sa.Column('city', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
