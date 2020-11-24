"""Add match participation table.

Revision ID: 015aaa0f37fd
Revises: ebcbc2e2e080
Create Date: 2020-11-10 15:59:21.993671

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '015aaa0f37fd'
down_revision = 'ebcbc2e2e080'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match_participants',
    sa.Column('tournament_id', sa.Integer(), nullable=True),
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['tournament_id', 'match_id'], ['matches.tournament_id', 'matches.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tournament_id', 'player_id'], ['team_members.tournament_id', 'team_members.player_id'], ),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournaments.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('match_id', 'player_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match_participants')
    # ### end Alembic commands ###