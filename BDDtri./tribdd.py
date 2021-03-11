from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017') #Connexion à la base données
db = client["db"] #Pointe le nom de la base de données
temperature = db.AHT20 #Select the collection name
humidite=db.AHT20
lmt335=db.LMT335
temperature_1 = db.AHT20.find().sort("temperature", -1).limit(1)


def lastValueTemperatrue():

    temperature_1 = db.AHT20.find().sort("temperature", -1).limit(1)
    for x in temperature_1:
        
        return x
def lastValuehumidity():

    humidite_1= db.AHT20.find().sort("humidite", -1).limit(1)
    for x in humidite_1:
        return x
def lastValuelm335 ():
    lmt335_1= db.LMT335.find().sort("temperature", -1).limit(1)
    for x in lmt335_1:
        return x



temperature=lastValueTemperatrue().get("temperature")
humidite=lastValuehumidity().get('humidite')
lmt335=lastValuelm335().get('temperature')
print(temperature)
print(humidite)
print(lmt335)
