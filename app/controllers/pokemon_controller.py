from flask import Blueprint,  jsonify
from app.models.factory import ModelFactory
from bson import ObjectId
from marshmallow import ValidationError

bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")
pokemon_model = ModelFactory.get_model("pokemons")

@bp.route("/get_pokemons", methods=["GET"])
def get_pokemons():
    try:
        pokemon = pokemon_model.find_all()
        return jsonify(pokemon, 200)
    except ValidationError as err:
        return jsonify("Hubo un error y no se cual es jeje", 400)
    
@bp.route("/get_pokemons/<string:pokemon_id", methods=["GET"])
def get_pokemons_id(pokemon_id):
    try:
        pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
        return jsonify(pokemon, 200)
    except ValidationError as err:
        return jsonify("Hubo un error y no se cual es jeje", 400)