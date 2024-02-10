from pymongo import MongoClient
import os
MONGO_URI = str(os.getenv('MONGO_URI'))
client = MongoClient(MONGO_URI)
db = client['Pokedex']
gen9_collection = db['Gen9']
type_collection = db['Type']
ability_collection = db['Ability']
