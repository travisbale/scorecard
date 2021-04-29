"""Add matches table.

Revision ID: ebcbc2e2e080
Revises: bd85d5151d12
Create Date: 2020-11-10 15:07:05.463781

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "ebcbc2e2e080"
down_revision = "bd85d5151d12"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "matches",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tournament_id", sa.Integer(), nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.Column("tee_color_id", sa.Integer(), nullable=False),
        sa.Column("match_format_id", sa.Integer(), nullable=False),
        sa.Column("tee_time", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id", "tee_color_id"],
            ["tee_sets.course_id", "tee_sets.tee_color_id"],
            ondelete="CASCADE",
            name="fk__matches__tee_sets",
        ),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"], name="fk__matches__course_id__courses"),
        sa.ForeignKeyConstraint(
            ["match_format_id"], ["match_formats.id"], name="fk__matches__match_format_id__match_formats"
        ),
        sa.ForeignKeyConstraint(["tee_color_id"], ["tee_colors.id"], name="fk__matches__tee_color_id__tee_colors"),
        sa.ForeignKeyConstraint(
            ["tournament_id"], ["tournaments.id"], ondelete="CASCADE", name="fk__matches__tournament_id__tournaments"
        ),
        sa.UniqueConstraint("id", "tournament_id", name="uq__matches__tournament_id"),
        sa.PrimaryKeyConstraint("id", name="pk__matches"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("matches")
    # ### end Alembic commands ###
