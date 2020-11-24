"""Tests for the match format model and schema."""

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models.match_format import MatchFormat, MatchFormatSchema


@pytest.fixture
def invalid_format(rollback_db):
    match_format = MatchFormat("format", "description")
    yield match_format

    with pytest.raises(IntegrityError):
        match_format.save()


@pytest.fixture(scope="module")
def schema():
    return MatchFormatSchema()


@pytest.fixture
def invalid_format_dict(schema):
    format_dict = dict(name="format", description="description")
    yield format_dict

    with pytest.raises(ValidationError):
        schema.load(format_dict)


def test_create_new_match_format():
    match_format = MatchFormat("a format", "a description")
    assert match_format.name == "a format"
    assert match_format.description == "a description"


def test_saving_match_format_with_duplicate_name_raises_integrity_error(invalid_format):
    MatchFormat("format", "description").save()


def test_saving_match_format_without_name_raises_integrity_error(invalid_format):
    invalid_format.name = None


def test_saving_match_format_without_description_raises_integrity_error(invalid_format):
    invalid_format.description = None


def test_match_format_schema_load_returns_match_format_instance(schema):
    match_format = schema.load(dict(name="format", description="description"))
    assert isinstance(match_format, MatchFormat)


def test_match_format_schema_raises_validation_error_if_dictionary_has_no_name_property(invalid_format_dict):
    invalid_format_dict["name"] = None


def test_match_format_schema_raises_validation_error_if_dictionary_has_no_description_property(invalid_format_dict):
    invalid_format_dict["description"] = None


def test_match_format_schema_raises_validation_error_if_dictionary_has_an_id_property(invalid_format_dict):
    invalid_format_dict["id"] = 1


def test_match_format_schema_dump(schema, rollback_db):
    match_format = MatchFormat("format", "description").save()
    dict = schema.dump(match_format)

    assert dict["id"] is not None and dict["id"] == match_format.id
    assert dict["name"] is not None and dict["name"] == match_format.name
    assert dict["description"] is not None and dict["description"] == match_format.description
