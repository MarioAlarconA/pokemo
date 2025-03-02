from flask import Blueprint
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required

RM = ResponseManager()
bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")
pokemon_model = ModelFactory.get_model("pokemons")

@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    data = pokemon_model.find_all()
    return RM.success(data)
   
    
@bp.route("/get_pokemons/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
        pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
        return RM.success(pokemon)
