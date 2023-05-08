from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# pikachu = {"name": "Pikachu"}
pikachu_query_result = pokemonColl.find_one({"name": "Pikachu"})
print(pikachu_query_result)

#  query that returns all the Pokemon with an attack greater than 150
attack_greater_150 = {"attack": {"$gt": 150}}
attack_result = pokemonColl.find(attack_greater_150)
print("Pokemon with attack greater than 150: ")
for result in attack_result:
   print(result)
    
# query that returns all the Pokemon with an ability of "Overgrow"
ability_overgrow = {"abilities": "Overgrow"}
ability_result = pokemonColl.find(ability_overgrow)
for result in ability_result:
  print(result)

