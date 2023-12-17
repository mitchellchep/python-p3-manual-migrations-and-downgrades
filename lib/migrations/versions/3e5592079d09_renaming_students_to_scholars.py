"""Renaming students to scholars

Revision ID: 3e5592079d09
Revises: 791279dd0760
Create Date: 2023-12-17 22:41:50.854231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e5592079d09'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
