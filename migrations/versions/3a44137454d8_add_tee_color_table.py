"""Add tee color table.

Revision ID: 3a44137454d8
Revises: 243cf8822dab
Create Date: 2020-11-10 03:27:39.671371

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3a44137454d8"
down_revision = "aba0d41f33eb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tee_colors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("color", sa.String(length=16), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk__tee_colors"),
        sa.UniqueConstraint("color", name="uq__tee_colors__color"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tee_colors")
    # ### end Alembic commands ###
