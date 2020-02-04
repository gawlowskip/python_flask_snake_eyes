import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
create foo table

Revision ID: da5234bc0825
Revises: 
Create Date: 2020-02-04 10:27:35.779416
"""

# Revision identifiers, used by Alembic.
revision = 'da5234bc0825'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('foos',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('created_on', AwareDateTime(),
                              default=tzware_datetime),
                    sa.Column('updated_on', AwareDateTime(),
                              default=tzware_datetime,
                              onupdate=tzware_datetime),
                    sa.Column('bar', sa.String(128), index=True))


def downgrade():
    op.drop_table('foos')
