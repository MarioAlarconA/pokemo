""" Crea
Elimina
Modifica la clase del modelo y evitar que se usen metodos indevidos """

from flask import Blueprint, request, jsonify 
from app.tools.response_manager import ResponseManager
from app.schemas.poke_fav_schema import PokeFavSchema
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import  ModelFactory

bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemons-favorites")
RM = ResponseManager()
FP_MODEL = ModelFactory.get_model("pokemons_favorites")
FP_SCHEMA = PokeFavSchema()

@bp.route ("/", methods=["POST"])
def create ():
    try:
        data = request.json
        data = FP_SCHEMA.validate(data)
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Envia todos lo parametros")
    

@bp.route("/<string:id>", methods=["DELETE"])
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = FP_MODEL.find_all()
    return RM.success(data)


""" from app.schemas.poke_fav_schema import PokeFavSchema
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
    return jsonify(pokemon, 200) """