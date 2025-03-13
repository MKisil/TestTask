from app import ma
from marshmallow import fields, validate

from app.users.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    created_at = ma.auto_field(dump_only=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
