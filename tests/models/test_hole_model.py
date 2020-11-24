"""Test the Hole model and schema."""

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models import Hole
from scorecard.models.course import Course
from scorecard.models.hole import HoleSchema
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


class TestHole:
    tee_color = None
    course = None
    tee_set = None

    @pytest.fixture
    def create_models(self, rollback_db):
        self.tee_color = TeeColor("white").save()
        self.course = Course("golf course").save()
        self.tee_set = TeeSet(self.tee_color.id, 113, 72, self.course.id).save()

    @pytest.fixture
    def hole(self, create_models):
        return Hole(1, 4, 3, 421, self.course.id, self.tee_color.id)

    @pytest.fixture
    def invalid_hole(self, hole, rollback_db):
        yield hole

        with pytest.raises(IntegrityError):
            hole.save()

    def test_create_new_hole(self):
        hole = Hole(1, 5, 6, 512, 2, 3)
        assert hole.number == 1
        assert hole.par == 5
        assert hole.hdcp == 6
        assert hole.yards == 512
        assert hole.course_id == 2
        assert hole.tee_color_id == 3

    def test_save_hole_without_a_tee_set_results_in_foreign_key_exception(self, invalid_hole):
        self.tee_set.delete()

    def test_save_hole_without_a_course_results_in_a_foreign_key_exception(self, invalid_hole):
        invalid_hole.course_id = 0

    def test_save_hole_without_a_tee_color_results_in_a_foreign_key_exception(self, invalid_hole):
        invalid_hole.tee_color_id = 0

    def test_save_hole_with_number_less_than_one_raises_integrity_error(self, invalid_hole):
        invalid_hole.number = 0

    def test_save_hole_with_number_greater_than_18_raises_integrity_error(self, invalid_hole):
        invalid_hole.number = 19

    def test_save_hole_with_hdcp_less_than_one_raises_integrity_error(self, invalid_hole):
        invalid_hole.hdcp = 0

    def test_save_hole_with_hdcp_greater_than_18_raises_integrity_error(self, invalid_hole):
        invalid_hole.hdcp = 19

    def test_save_hole_with_par_less_than_3_raises_integrity_error(self, invalid_hole):
        invalid_hole.par = 2

    def test_save_hole_with_par_greater_than_6_raises_integrity_error(self, invalid_hole):
        invalid_hole.par = 7

    def test_save_duplicate_hole_number_raises_integrity_error(self, invalid_hole):
        Hole(1, 4, 1, 421, self.course.id, self.tee_color.id).save()

    def test_save_duplicate_hole_hdcp_raises_integrity_error(self, invalid_hole):
        Hole(2, 4, 3, 421, self.course.id, self.tee_color.id).save()

    def test_save_hole_without_par_raises_integrity_error(self, invalid_hole):
        invalid_hole.par = None

    def test_save_hole_without_hdcp_raises_integrity_error(self, invalid_hole):
        invalid_hole.hdcp = None

    def test_save_hole_without_yards_raises_integrity_error(self, invalid_hole):
        invalid_hole.yards = None

    def test_save_valid_hole_persists_it_to_the_database(self, hole):
        hole.save()
        assert Hole.query.get((hole.course_id, hole.tee_color_id, 1)) is not None

    def test_delete_tee_set_also_deletes_the_hole(self, hole):
        hole.save()
        self.tee_set.delete()
        assert Hole.query.get((hole.course_id, hole.tee_color_id, 1)) is None

    def test_hole_schema_dump_serializes_hole(self, hole):
        hole_dict = HoleSchema().dump(hole.save())
        assert hole_dict["number"] == hole.number
        assert hole_dict["par"] == hole.par
        assert hole_dict["hdcp"] == hole.hdcp
        assert hole_dict["yards"] == hole.yards


class TestHoleSchema:
    @pytest.fixture(scope="class")
    def schema(self):
        return HoleSchema()

    @pytest.fixture
    def invalid_dict(self, schema):
        hole = dict(number=1, par=5, hdcp=1, yards=513)
        yield hole

        with pytest.raises(ValidationError):
            schema.load(hole)

    def test_hole_schema_load_hole_returns_hole_instance(self, schema):
        hole = schema.load(dict(number=1, par=5, hdcp=1, yards=512))
        assert isinstance(hole, Hole)

    def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_number_property(self, invalid_dict):
        invalid_dict["number"] = None

    def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_par_property(self, invalid_dict):
        invalid_dict["par"] = None

    def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_hdcp_property(self, invalid_dict):
        invalid_dict["hdcp"] = None

    def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_yards_property(self, invalid_dict):
        invalid_dict["yards"] = None
