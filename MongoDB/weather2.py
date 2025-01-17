# https://openweathermap.org/current

# You will need to create a variable WEATHER with your key of OpenWeatherMap in your console with the export command
# You can choose the city of your choice, you only need to write the name in english

from pymongo import MongoClient
import os
import requests
from datetime import datetime
# lisibilité
from pprint import pprint

KEY = os.getenv("WEATHER")
assert KEY is not None

def make_data(city):
    r = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
            city, KEY
        )
    )
    data = r.json()
    clean_data = {i: data[i] for i in ["weather", "main"]}
    clean_data["weather"] = clean_data["weather"][0]
    return clean_data


def add_key(data, city):
    current = datetime.now().strftime("%H:%M:%S")
    data["time"] = current
    data["city"] = city

    return data


def add_data(client, cities):

    col = client["sample"]["weather"]

    for city in cities:
        data = make_data(city)
        data = add_key(data, city)
        col.insert_one(data)

def p(l):
    pprint(list(l))

client = MongoClient(host="localhost", port=27017, username="datascientest", password="dst123")

add_data(client, ["courbevoie", "puteaux", "lourdes","bourg-la-reine"])
col = client['sample']['weather']

pprint(list(col.find({'weather.main':'Clear'}, {'city':1,'_id':0})))

# Combien de documents ont une valeur de clé temp_min supérieure ou égale à 289 et une valeur de clé temp_max inférieure à égale à 291. (Les températures sont en Kelvin)

print(
    len(
        list(
            col.find(
                {
                    "$and": [
                        {"main.temp_min": {"$gte": 274}},
                        {"main.temp_max": {"$lte": 276}},
                    ]
                }
            )
        )
    )
)

print(
    col.count_documents(
        {
            "$and": [
                {"main.temp_min": {"$gte": 274}},
                {"main.temp_max": {"$lte": 276}},
            ]
        }
    )
)

# With the implicit AND

print(
    col.count_documents(
        {"main.temp_min": {"$gte": 274}, "main.temp_max": {"$lte": 276}},
    )
)

p(col.find({},
    {'weather.main'}
))

p(col.aggregate([
    {'$group':{'_id': '$weather.main', 'nb':{'$sum': 1}}}
]))
