"""Unit tests for the match class."""

from datetime import datetime

from scorecard.models import Match


class TestMatchModel:
    """Test the match model."""

    def test_create_new_match(self):
        """Test create new match."""
        now = datetime.now()
        match = Match(1, 1, 1, now)
        assert match.course_id == 1
        assert match.tee_color_id == 1
        assert match.match_format_id == 1
        assert match.tee_time == now
