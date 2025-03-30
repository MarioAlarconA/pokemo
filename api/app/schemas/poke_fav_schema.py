
from marshmallow import Schema, fields

class PokeFavSchema(Schema):
    pokemon_id = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El ID es requerido"
        }
    )