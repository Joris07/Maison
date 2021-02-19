from pymongo import MongoClient
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

def on_message_print(client, userdata, message):
    tropic= message.topic
    data = message.payload.decode()
    tab = tropic.split("/")
    monDico= { }
    print(tab[0])
    if(tab[1].find("temperature")!=-1):
        monDico[tab[1]]=data
    elif(tab[1].find("humidite")!=-1):
        monDico[tab[1]]=data
    insert_bdd(tab[0], monDico)

def insert_bdd(topic,dico):
    if(str(topic)=="AHT20"):
        col = db.AHT20
        col.insert(dico)
        client.close()
    elif(str(topic)=="AHT10"):
        col = db.AHT10
        col.insert(dico)
        client.close()

subscribe.callback(on_message_print, "#", hostname="172.20.78.137")
