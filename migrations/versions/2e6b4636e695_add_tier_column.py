"""Add tier column to player table

Revision ID: 2e6b4636e695
Revises: ed194719e10b
Create Date: 2021-05-13 17:38:15.407858

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2e6b4636e695"
down_revision = "ed194719e10b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("players", sa.Column("tier", sa.String(length=32), nullable=True))
    op.execute("UPDATE players SET tier = 'white'")
    op.alter_column("players", "tier", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("players", "tier")
    # ### end Alembic commands ###
