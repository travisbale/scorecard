"""Match scores module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.hole import Hole
from scorecard.models.match import Match
from scorecard.models.match_participant import MatchParticipant
from scorecard.models.score import Score, ScoreSchema
from scorecard.resources.view_decorators import permission_required
from werkzeug.exceptions import BadRequest

schema = ScoreSchema()


class HoleScoresResource(MethodView):
    """Dispatches request methods to view or modify the scores for a particular hole."""

    def get(self, match_id, hole_number):
        """Return the scores for each player on a hole in a given match."""
        self._check_route_parameters(match_id, hole_number)
        scores = Score.query.filter_by(match_id=match_id, hole_number=hole_number)
        return jsonify(schema.dump(scores, many=True)), HTTPStatus.OK

    @permission_required("create:scores")
    def post(self, match_id, hole_number):
        """Record players' scores in a match."""
        match = self._check_route_parameters(match_id, hole_number)
        scores = schema.load(request.get_json(), many=True)

        participants = MatchParticipant.query.filter(
            MatchParticipant.player_id.in_(map(lambda score: score.player_id, scores)),
            MatchParticipant.match_id == match_id,
        )

        if len(scores) != participants.count():
            raise BadRequest(description="One or more players are not in the match.")

        for score in scores:
            score.match_id = match_id
            score.course_id = match.course_id
            score.tee_color_id = match.tee_color_id
            score.hole_number = hole_number
            score.merge()

        return jsonify(message="The scores have been recorded"), HTTPStatus.CREATED

    def _check_route_parameters(self, match_id, hole_number):
        match = Match.query.get_or_404(match_id, "Them match does not exist")
        Hole.query.get_or_404((match.course_id, match.tee_color_id, hole_number), "The hole does not exist")

        return match


class MatchScoresResource(MethodView):
    """Dispatches request methods to view the scores for a particlar match."""

    def get(self, match_id):
        """Return all the scores for a player in a given match."""
        Match.query.get_or_404(match_id, "The match does not exist.")
        scores = Score.query.filter_by(match_id=match_id)
        return jsonify(schema.dump(scores, many=True)), HTTPStatus.OK


def register_resources(bp):
    """Add the resources routes to the application blueprint."""
    bp.add_url_rule(
        "/matches/<int:match_id>/holes/<int:hole_number>/scores",
        view_func=HoleScoresResource.as_view("hole_scores_resource"),
    )
    bp.add_url_rule(
        "/matches/<int:match_id>/scores",
        view_func=MatchScoresResource.as_view("player_scores_resource"),
    )
