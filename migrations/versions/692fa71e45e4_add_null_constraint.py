"""add null constraint

Revision ID: 692fa71e45e4
Revises: 73a0557bbf16
Create Date: 2020-11-24 06:33:58.220198

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "692fa71e45e4"
down_revision = "73a0557bbf16"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("match_participants", "tournament_id", existing_type=sa.INTEGER(), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("match_participants", "tournament_id", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###
