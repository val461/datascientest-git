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
CITY = "COURBEVOIE"

assert KEY is not None

r = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        CITY, KEY
    )
)

current = datetime.now().strftime("%H:%M:%S")
data = r.json()
pprint(data)

input('[enter] ')

clean_data = {i: data[i] for i in ["weather", "main"]}
clean_data["weather"] = clean_data["weather"][0]
clean_data["time"] = current
clean_data["city"] = CITY
pprint(clean_data)

input('[enter] ')

client = MongoClient(host="localhost", port=27017, username="datascientest", password="dst123")
sample = client["sample"]
col = sample.create_collection(name="weather")
col.insert_one(clean_data)

input('[enter] ')

for c in ['PARIS','REIMS']:
    r = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
            c, KEY
        )
    )
    current = datetime.now().strftime("%H:%M:%S")
    data = r.json()
    clean_data = {i: data[i] for i in ["weather", "main"]}
    clean_data["weather"] = clean_data["weather"][0]
    clean_data["time"] = current
    clean_data["city"] = c
    col.insert_one(clean_data)


