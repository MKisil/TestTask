from marshmallow import ValidationError


def validate_user_data(schema, data):
    try:
        validated_data = schema.load(data)
        return validated_data, None
    except ValidationError as err:
        return None, err.messages


def email_exists(model, email):
    return model.query.filter_by(email=email).first() is not None
