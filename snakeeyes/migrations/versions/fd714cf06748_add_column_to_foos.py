import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add column to foos

Revision ID: fd714cf06748
Revises: da5234bc0825
Create Date: 2020-02-04 11:12:43.823038
"""

# Revision identifiers, used by Alembic.
revision = 'fd714cf06748'
down_revision = 'da5234bc0825'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('foos', sa.Column('hello_on', AwareDateTime(),
                                    default=tzware_datetime))


def downgrade():
    op.drop_column('foos', 'hello_on')
