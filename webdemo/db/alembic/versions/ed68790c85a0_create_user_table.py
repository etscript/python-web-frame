"""Create user table

Revision ID: ed68790c85a0
Revises: 
Create Date: 2018-03-02 13:14:50.840776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed68790c85a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(64), nullable=False, unique=True),
        sa.Column('gender', sa.String(64), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
        sa.Column('email', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
