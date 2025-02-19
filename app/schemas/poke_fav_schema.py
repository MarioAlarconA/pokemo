
from marshmallow import Schema, fields

class PokeFavSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre es requerido"
        }
    )