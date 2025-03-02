""" Crea
Elimina
Modifica la clase del modelo y evitar que se usen metodos indevidos """

from flask import Blueprint, request, jsonify 
from app.tools.response_manager import ResponseManager
from app.schemas.poke_fav_schema import PokeFavSchema
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import  ModelFactory
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemons-favorites")
RM = ResponseManager()
FP_MODEL = ModelFactory.get_model("pokemons_favorites")
FP_SCHEMA = PokeFavSchema()

@bp.route ("/", methods=["POST"])
@jwt_required()
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
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)
