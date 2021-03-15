from flask import abort


def check_type(variable, type_):
    if not isinstance(variable, type_):
        abort(400, f"Payload has to be of type {type_}")


def validate_payload(payload, schema):
    check_type(payload, dict)

    for key, value in payload.items():
        if key in schema:
            check_type(value, schema[key])
