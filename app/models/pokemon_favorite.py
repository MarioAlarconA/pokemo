from app import mongo
from app.models.super_clase import SuperClass
from bson import ObjectId

class PokemonFavorites(SuperClass):
    def __init__(self):
        super().__init__("pokemon_favorites")
    
    def update(self, object_id, data):
        raise NotImplementedError("No se puede actualizar")
    
    def find_by_id(self, object_id):
        raise NotImplementedError("No se puede encontrar")
    
    def update(self, user_id):
        data = self.collection.find({"user_id": ObjectId(user_id)})
        return data
    
    def find_all(self,user_id):
        data = list(self.collection.find({"user_id": ObjectId(user_id)}))
        for datum in data:
            datum["user_id"] = str(datum["user_id"])
            datum["pokemons_id"] = str(datum["pokemons_id"])
            datum["_id"] = str(datum["_id"])
        return data
    
    def create(self, data):
        data["user_id"] = ObjectId(data["user_id"])
        data["pokemon_id"] = ObjectId(data["pokemon_id"])
        datum = self.collection.insert_one(data)
        return str(datum.inserted_id)