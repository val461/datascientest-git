# https://pymongo.readthedocs.io/en/stable/
from pymongo import MongoClient

# optionnel, pour la lisibilité
from pprint import pprint

import re

client = MongoClient(
    host = "127.0.0.1",
    port = 27017,
    username = "datascientest",
    password = "dst123"
)

# comme `show dbs` sur le MongoDB Shell
print(client.list_database_names())

# sélectionnons la base de données sample
sample = client["sample"]

print(sample.list_collection_names())

zips = sample["zips"]
#zips = client["sample"]['zips']
print(zips.find_one())

# créer une collection avec le nom rand
rand = sample.create_collection(name="rand")

# We can check the creation of the collection with this
print(sample.list_collection_names())

data = [
  {"name": "Melthouse","bread":"Wheat","sauce": "Ceasar"},
  {"name": "Italian BMT", "extras": ["pickles","onions","lettuce"],"sauce":["Chipotle", "Aioli"]},
  {"name": "Steakhouse Melt","bread":"Parmesan Oregano"},
  {"name": "Germinal", "author":"Emile Zola"},
  {"pastry":"cream puff","flavour":"chocolate","size":"big"}
]

rand.insert_many(data)

input('[enter] ')

for i in list(zips.find({},{"_id":0,"city":1})):
    print(i)

input('[enter] ')

for i in list(zips.find({},{"_id":0,"city":1}).limit(12)):
    print(i)

print(zips.find().distinct("state"))

input('[enter] ')

pprint(client["sample"]["cie"].find_one())

# noms des documents dont les villes ne sont que des nombres
regex = re.compile("^[0-9]*$")
pprint(list(zips.find({"city": regex}, {"city": 1})))

# nom de la société qui a acquis la société Tumblr
pprint(
    list(
        client["sample"]["cie"].aggregate(
            [
                {"$match": {"acquisitions.company.name": "Tumblr"}},
                {"$project": {"_id": 1, "society": "$name"}}
            ]
        )
    )
)
