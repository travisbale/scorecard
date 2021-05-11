"""Message schema module."""

from marshmallow import Schema, fields


class InvitationEmailSchema(Schema):
    """These fields are used to populate the email template."""

    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    url = fields.String()
