"""Tests for the match format model and schema."""

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models.match_format import MatchFormat, MatchFormatSchema


class TestMatchFormat:
    @pytest.fixture
    def match_format(self):
        return MatchFormat("format", "description")

    @pytest.fixture
    def invalid_format(self, match_format, rollback_db):
        yield match_format

        with pytest.raises(IntegrityError):
            match_format.save()

    def test_create_new_match_format(self, match_format):
        assert match_format.name == "format"
        assert match_format.description == "description"

    def test_save_duplicate_name_raises_integrity_error(self, invalid_format):
        MatchFormat("format", "description").save()

    def test_save_without_name_raises_integrity_error(self, invalid_format):
        invalid_format.name = None

    def test_save_without_description_raises_integrity_error(self, invalid_format):
        invalid_format.description = None

    def test_match_format_schema_dump(self, match_format, rollback_db):
        format_dict = MatchFormatSchema().dump(match_format.save())
        assert format_dict["id"] == match_format.id
        assert format_dict["name"] == match_format.name
        assert format_dict["description"] == match_format.description


class TestMatchFormatSchema:
    @pytest.fixture(scope="class")
    def schema(self):
        return MatchFormatSchema()

    @pytest.fixture
    def invalid_dict(self, schema):
        format_dict = dict(name="format", description="description")
        yield format_dict

        with pytest.raises(ValidationError):
            schema.load(format_dict)

    def test_load_returns_match_format_instance(self, schema):
        match_format = schema.load(dict(name="format", description="description"))
        assert isinstance(match_format, MatchFormat)

    def test_load_raises_validation_error_if_dictionary_has_no_name_property(self, invalid_dict):
        invalid_dict["name"] = None

    def test_load_raises_validation_error_if_dictionary_has_no_description_property(self, invalid_dict):
        invalid_dict["description"] = None

    def test_load_raises_validation_error_if_dictionary_has_an_id_property(self, invalid_dict):
        invalid_dict["id"] = 1
