"""Test the Hole model and schema."""

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard import db
from scorecard.models import Hole
from scorecard.models.course import Course
from scorecard.models.hole import HoleSchema
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet

course = None
tee_color = None
tee_set = None


@pytest.fixture(scope="module")
def models():
    tee_color = TeeColor("white").save()
    course = Course("golf course").save()
    tee_set = TeeSet(tee_color.id, 113, 72, course.id).save()
    db.session.commit()
    yield dict(tee_color=tee_color, course=course, tee_set=tee_set)
    tee_set.delete()
    tee_color.delete()
    course.delete()
    db.session.commit()


@pytest.fixture
def invalid_hole(models, rollback_db):
    hole = Hole(1, 5, 2, 512, models["course"].id, models["tee_color"].id)

    yield hole

    with pytest.raises(IntegrityError):
        hole.save()


@pytest.fixture
def hole(models):
    return Hole(1, 4, 3, 421, models["course"].id, models["tee_color"].id)


@pytest.fixture(scope="module")
def schema():
    return HoleSchema()


@pytest.fixture
def invalid_hole_dict(schema):
    hole = dict(number=1, par=5, hdcp=1, yards=513)

    yield hole

    with pytest.raises(ValidationError):
        schema.load(hole)


def test_create_new_hole():
    hole = Hole(1, 5, 6, 512, 2, 3)
    assert hole.number == 1
    assert hole.par == 5
    assert hole.hdcp == 6
    assert hole.yards == 512
    assert hole.course_id == 2
    assert hole.tee_color_id == 3


def test_save_hole_without_a_tee_set_results_in_foreign_key_exception(models, invalid_hole):
    models["tee_set"].delete()


def test_save_hole_without_a_course_results_in_a_foreign_key_exception(models, invalid_hole):
    invalid_hole.course_id = 0


def test_save_hole_without_a_tee_color_results_in_a_foreign_key_exception(invalid_hole):
    invalid_hole.tee_color_id = 0


def test_save_hole_with_number_less_than_one_raises_integrity_error(invalid_hole):
    invalid_hole.number = 0


def test_save_hole_with_number_greater_than_18_raises_integrity_error(invalid_hole):
    invalid_hole.number = 19


def test_save_hole_with_hdcp_less_than_one_raises_integrity_error(invalid_hole):
    invalid_hole.hdcp = 0


def test_save_hole_with_hdcp_greater_than_18_raises_integrity_error(invalid_hole):
    invalid_hole.hdcp = 19


def test_save_hole_with_par_less_than_3_raises_integrity_error(invalid_hole):
    invalid_hole.par = 2


def test_save_hole_with_par_greater_than_6_raises_integrity_error(invalid_hole):
    invalid_hole.par = 7


def test_save_duplicate_hole_number_raises_integrity_error(models, invalid_hole):
    hole = Hole(1, 4, 3, 421, models["course"].id, models["tee_color"].id)
    hole.save()


def test_save_duplicate_hole_hdcp_raises_integrity_error(models, invalid_hole):
    hole = Hole(2, 4, 2, 421, models["course"].id, models["tee_color"].id)
    hole.save()


def test_save_hole_without_par_raises_integrity_error(invalid_hole):
    invalid_hole.par = None


def test_save_hole_without_hdcp_raises_integrity_error(invalid_hole):
    invalid_hole.hdcp = None


def test_save_hole_without_yards_raises_integrity_error(invalid_hole):
    invalid_hole.yards = None


def test_save_valid_hole_persists_it_to_the_database(hole, rollback_db):
    hole.save()
    assert Hole.query.get((hole.course_id, hole.tee_color_id, 1)) is not None


def test_delete_tee_set_also_deletes_the_hole(models, hole, rollback_db):
    hole.save()
    # Delete the tee set and verify the hole no longer exists
    models["tee_set"].delete()
    assert Hole.query.get((hole.course_id, hole.tee_color_id, 1)) is None


def test_hole_schema_load_hole_returns_hole_instance(schema):
    hole = schema.load(dict(number=1, par=5, hdcp=1, yards=512))
    assert isinstance(hole, Hole)


def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_number_property(invalid_hole_dict):
    invalid_hole_dict["number"] = None


def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_par_property(invalid_hole_dict):
    invalid_hole_dict["par"] = None


def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_hdcp_property(invalid_hole_dict):
    invalid_hole_dict["hdcp"] = None


def test_hole_schema_load_raises_validation_error_if_dictionary_has_no_yards_property(invalid_hole_dict):
    invalid_hole_dict["yards"] = None


def test_hole_schema_dump(hole, schema, rollback_db):
    dict = schema.dump(hole.save())

    assert dict["number"] is not None and dict["number"] == hole.number
    assert dict["par"] is not None and dict["par"] == hole.par
    assert dict["hdcp"] is not None and dict["hdcp"] == hole.hdcp
    assert dict["yards"] is not None and dict["yards"] == hole.yards
