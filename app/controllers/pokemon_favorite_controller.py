""" Crea
Elimina
Modifica la clase del modelo y evitar que se usen metodos indevidos """

from flask import Blueprint, request, jsonify 
from app.schemas.poke_fav_schema import PokeFavSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
poke_fav_schema= PokeFavSchema()
pokemon_favorite_model = ModelFactory.getModel("pokemons_favorites")

@bp.route("/create", methods=["POST"])
def create():
    try:
        data = poke_fav_schema.load(request.json)
        pokemon_id= poke_fav_schema.create(data)
        return jsonify({"user_id":str(pokemon_id)}, 200)
    
    except ValidationError as error:
        return jsonify("Los parametros incorrectearon", 400)
    
    
@bp.route("/delete/<string:pokemon_id>", methods=["DELETE"])
def delete(pokemon_id):
    poke_fav_schema.delete(ObjectId(pokemon_id))
    return jsonify("Pokemon eliminado con exito", 200)

@bp.route("/get_pokemons/", methods=["GET"])
def get_pokemon():
    pokemon = pokemon_favorite_model.find_all()
    return jsonify(pokemon, 200)