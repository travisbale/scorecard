"""Test the BaseSchema class."""

from scorecard.models.base import BaseSchema


class FieldObj(object):
    """Helper class for testing the BaseSchema class."""

    def __init__(self, data_key=None):
        self.data_key = data_key


def test_on_bind_field_converts_data_key_property_to_camel_case():
    field_obj = FieldObj("snake_case_property")
    schema = BaseSchema()
    schema.on_bind_field("test", field_obj)

    assert field_obj.data_key == "snakeCaseProperty"


def test_on_bind_field_converts_field_name_to_camel_case():
    field_obj = FieldObj()
    schema = BaseSchema()
    schema.on_bind_field("snake_case_name", field_obj)

    assert field_obj.data_key == "snakeCaseName"
