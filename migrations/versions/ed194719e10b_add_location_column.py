"""Add location column to tournaments table

Revision ID: ed194719e10b
Revises: a9ab94977cf5
Create Date: 2021-05-13 14:37:46.261493

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ed194719e10b"
down_revision = "a9ab94977cf5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tournaments", sa.Column("location", sa.String(length=255), nullable=True))
    op.execute("UPDATE tournaments SET location=''")
    op.alter_column("tournaments", "location", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tournaments", "location")
    # ### end Alembic commands ###
