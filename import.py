# import sqlite 
import sqlite3
import sys
# connect to the appropriate table in the sqlite database
connectTable = sqlite3.connect('pokemon.sqlite')
connect = connectTable.cursor()
from pymongo import MongoClient

# Connect to MongoDB 
mongoClient = MongoClient('mongodb://localhost/pokemon')
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Get the information that you need in order to create the JSON shown in the readme
for i in range(1, 802):
   pokemonRow = connect.execute("SELECT * FROM pokemon WHERE id = " + str(i)).fetchone()
   pokemontype1 = connect.execute("SELECT * FROM type LEFT OUTER JOIN pokemon_type ON type.id = pokemon_type.type_id WHERE pokemon_type.pokemon_id = " + str(i)).fetchone()
   pokemontype2 = connect.execute("SELECT * FROM type LEFT OUTER JOIN pokemon_type ON type.id = pokemon_type.type_id WHERE pokemon_type.pokemon_id = " + str(i)).fetchone()
   abilities = connect.execute("SELECT * FROM ability LEFT OUTER JOIN pokemon_abilities ON ability.id = pokemon_abilities.ability_id WHERE pokemon_abilities.pokemon_id = " + str(i)).fetchone()
   # For each row in the result set, create a key-value pair array that stores all of the information regarding that pokemon (you just found this information in the query 
   # Insert the array into the MongoDB collection
   pokemon = {
         "name": pokemonRow[2],
         "pokedex_number": pokemonRow[1],
         "types": [pokemontype1[1],   
         pokemontype2[1]],
         "hp": pokemonRow[5],
         "attack": pokemonRow[6],
         "defense": pokemonRow[7],
         "speed": pokemonRow[8],
         "sp_attack": pokemonRow[9],
         "sp_defense": pokemonRow[10],
         "abilities": abilities
      }
   print(pokemon)
   pokemonColl.insert_one(pokemon)