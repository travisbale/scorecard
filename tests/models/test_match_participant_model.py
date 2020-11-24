"""Tests for the match participant model and schema."""

from datetime import datetime

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.match_participant import MatchParticipant, MatchParticipantSchema
from scorecard.models.player import Player
from scorecard.models.score import Score
from scorecard.models.team import Team
from scorecard.models.team_member import TeamMember
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet
from scorecard.models.tournament import Tournament


class TestMatchParticipant:
    tournament = None
    match = None
    player = None
    team_member = None
    course = None
    tee_color = None

    @pytest.fixture
    def create_models(self, rollback_db):
        self.tee_color = TeeColor("white").save()
        self.course = Course("course name").save()
        TeeSet(self.tee_color.id, 113, 72, self.course.id).save()

        team = Team("team name").save()
        self.player = Player("test@test.com", "John", "Smith", 10).save()
        self.tournament = Tournament("name", datetime.now(), datetime.now()).save()
        self.team_member = TeamMember(self.tournament.id, team.id, self.player.id, False).save()

        match_format = MatchFormat("name", "description").save()
        self.match = Match(self.course.id, self.tee_color.id, match_format.id, datetime.now(), self.tournament.id)
        self.match.save()

    @pytest.fixture
    def participant(self, create_models):
        return MatchParticipant(self.tournament.id, self.match.id, self.player.id)

    @pytest.fixture
    def invalid_participant(self, participant):
        yield participant

        with pytest.raises(IntegrityError):
            participant.save()

    @pytest.fixture
    def delete_participant(self, participant):
        participant.save()
        yield
        assert MatchParticipant.query.get((self.match.id, self.player.id)) is None

    def test_create_new_match_participant(self):
        participant = MatchParticipant(1, 2, 3)
        assert participant.tournament_id == 1
        assert participant.match_id == 2
        assert participant.player_id == 3

    def test_save_duplicate_raises_integrity_error(self, invalid_participant):
        MatchParticipant(self.tournament.id, self.match.id, self.player.id).save()

    def test_save_without_tournament_results_in_foreign_key_exception(self, invalid_participant):
        self.tournament.delete()

    def test_save_without_match_results_in_foreign_key_exception(self, invalid_participant):
        self.match.delete()

    def test_save_without_player_results_in_foreign_key_exception(self, invalid_participant):
        self.player.delete()

    def test_save_without_team_member_results_in_foreign_key_exception(self, invalid_participant):
        self.team_member.delete()

    def test_save_without_tournament_id_raises_integrity_error(self, invalid_participant):
        invalid_participant.tournament_id = None

    def test_delete_tournament_deletes_the_match_participant(self, delete_participant):
        self.tournament.delete()

    def test_delete_match_deletes_the_match_participant(self, delete_participant):
        self.match.delete()

    def test_delete_deletes_all_match_scores(self, participant):
        participant.save()
        hole = Hole(1, 5, 1, 513, self.course.id, self.tee_color.id).save()
        Score(self.player.id, 3, self.match.id, self.course.id, self.tee_color.id, hole.number).save()
        participant.delete()
        assert Score.query.get((self.match.id, self.player.id, hole.number)) is None

    def test_save_persists_match_participant_to_the_database(self, participant):
        participant.save()
        assert MatchParticipant.query.get((self.match.id, self.player.id)) is not None

    def test_dumping_schema_serializes_match_participant(self, participant):
        dictionary = MatchParticipantSchema().dump(participant.save())
        dictionary["team"] = "team name"
        dictionary["playerId"] = participant.player.id
        dictionary["lastName"] = participant.player.last_name
        dictionary["fullName"] = participant.player.full_name


class TestMatchParticipantSchema:
    @pytest.fixture(scope="class")
    def schema(self):
        return MatchParticipantSchema()

    @pytest.fixture
    def invalid_dict(self, schema):
        participants = dict(playerIds=[])
        yield participants

        with pytest.raises(ValidationError):
            schema.load(participants)

    def test_load_raises_validation_error_if_dict_has_no_player_ids(self, invalid_dict):
        invalid_dict["playerIds"] = None

    def test_load_raises_validation_error_if_dict_has_team(self, invalid_dict):
        invalid_dict["team"] = "name"

    def test_load_raises_validation_error_if_dict_has_player_id(self, invalid_dict):
        invalid_dict["playerId"] = 1

    def test_load_raises_validation_error_if_dict_has_last_name(self, invalid_dict):
        invalid_dict["lastName"] = "Smith"

    def test_load_raises_validation_error_if_dict_has_full_name(self, invalid_dict):
        invalid_dict["fullName"] = "John Smith"
