"""Test the match model and schema."""

from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError

from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.match_participant import MatchParticipant
from scorecard.models.player import Player
from scorecard.models.score import Score
from scorecard.models.team import Team
from scorecard.models.team_member import TeamMember
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet
from scorecard.models.tournament import Tournament


class TestMatch:
    tournament = None
    course = None
    tee_color = None
    match_format = None
    players = None

    @pytest.fixture
    def create_models(self, pebble_beach, rollback_db):
        self.tournament = Tournament("tournament name", datetime.now(), datetime.now()).save()
        self.course = pebble_beach
        self.tee_color = TeeColor.query.filter_by(color="White").first()
        self.match_format = MatchFormat("format name", "format description").save()

    @pytest.fixture
    def match(self, create_models):
        return Match(self.course.id, self.tee_color.id, self.match_format.id, datetime.now(), self.tournament.id)

    @pytest.fixture
    def create_participants(self, match):
        match.save()
        teams = [
            Team("Red").save(),
            Team("Blue").save(),
        ]
        self.players = {
            "Michael": Player("michael@test.com", "Michael", "Scott", 10).save(),
            "Jim": Player("jim@test.com", "Jim", "Halpert", 3).save(),
            "Dwight": Player("dwight@test.com", "Dwight", "Schrute", 5).save(),
            "Andy": Player("andy@test.com", "Andy", "Bernard", 7).save(),
        }

        TeamMember(self.tournament.id, teams[0].id, self.players["Michael"].id).save(),
        TeamMember(self.tournament.id, teams[0].id, self.players["Jim"].id).save(),
        TeamMember(self.tournament.id, teams[1].id, self.players["Dwight"].id).save(),
        TeamMember(self.tournament.id, teams[1].id, self.players["Andy"].id).save(),

        MatchParticipant(self.tournament.id, match.id, self.players["Michael"].id).save(),
        MatchParticipant(self.tournament.id, match.id, self.players["Jim"].id).save(),
        MatchParticipant(self.tournament.id, match.id, self.players["Dwight"].id).save(),
        MatchParticipant(self.tournament.id, match.id, self.players["Andy"].id).save(),

    @pytest.fixture
    def invalid_match(self, match):
        yield match

        with pytest.raises(IntegrityError):
            match.save()

    def test_create_new_match(self):
        now = datetime.now()
        match = Match(1, 2, 3, now, 4)

        assert match.course_id == 1
        assert match.tee_color_id == 2
        assert match.match_format_id == 3
        assert match.tee_time == now
        assert match.tournament_id == 4

    def test_save_without_tournament_id_raises_integrity_error(self, invalid_match):
        invalid_match.tournament_id = None

    def test_save_without_course_id_raises_integrity_error(self, invalid_match):
        invalid_match.course_id = None

    def test_save_without_tee_color_id_raises_integrity_error(self, invalid_match):
        invalid_match.tee_color_id = None

    def test_save_without_match_format_id_raises_integrity_error(self, invalid_match):
        invalid_match.match_format_id = None

    def test_save_without_tee_set_raises_integrity_error(self, invalid_match):
        TeeSet.query.get((self.course.id, self.tee_color.id)).delete()

    def test_delete_tournament_deletes_match(self, match):
        match.save()
        self.tournament.delete()
        assert Match.query.get(match.id) is None

    def test_delete_deletes_all_match_participants(self, match):
        player = Player("test@test.com", "John", "Smith", 10).save()
        team = Team("team name").save()
        TeamMember(self.tournament.id, team.id, player.id).save()
        MatchParticipant(self.tournament.id, match.save().id, player.id).save()
        match.delete()
        assert MatchParticipant.query.get((match.id, player.id)) is None

    def test_get_team_members_returns_the_members_of_the_team(self, match, create_participants):
        players = list(map(lambda participant: participant.player, match.get_team_members("Red")))
        assert len(players) == 2
        assert players[0].first_name == "Michael" or players[1].first_name == "Michael"
        assert players[0].first_name == "Jim" or players[1].first_name == "Jim"

    def test_started_returns_false_until_everyone_has_recorded_a_score(self, match, create_participants):
        self.create_scores("Michael", match.id, [4])
        self.create_scores("Jim", match.id, [4])
        self.create_scores("Dwight", match.id, [4])

        assert not match.started()

    def test_started_returns_true_once_everyone_has_recorded_a_score(self, match, create_participants):
        self.create_scores("Michael", match.id, [4])
        self.create_scores("Jim", match.id, [4])
        self.create_scores("Dwight", match.id, [4])
        self.create_scores("Andy", match.id, [4])

        assert match.started()

    def test_score_returns_all_square_if_the_match_is_tied(self, match, create_participants):
        self.create_scores("Michael", match.id, [4, 4, 4, 4])
        self.create_scores("Jim", match.id, [4, 4, 4, 4])
        self.create_scores("Dwight", match.id, [4, 4, 4, 4])
        self.create_scores("Andy", match.id, [4, 4, 4, 4])
        scores = match.scores

        assert scores[-1]["matchStatus"] == 0
        assert scores[-1]["statusText"] == "AS"

    def test_score_returns_blue_lead_if_blue_is_in_the_lead(self, match, create_participants):
        scores1 = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 4, 3, 3, 4, 3, 4, 4, 4]
        scores2 = [5, 4, 5, 4, 3, 4, 4, 4, 5, 5, 4, 3, 4, 4, 4, 5, 4, 4]
        self.create_scores("Michael", match.id, scores1)
        self.create_scores("Jim", match.id, scores2)
        self.create_scores("Dwight", match.id, scores2)
        self.create_scores("Andy", match.id, scores2)

        scores = match.scores

        assert scores[-1]["matchStatus"] == 8
        assert scores[-1]["statusText"] == "6 & 5"

    def create_scores(self, name, match_id, scores):
        for hole_number, score in enumerate(scores):
            Score(self.players[name].id, score, match_id, self.course.id, self.tee_color.id, hole_number + 1).merge()
