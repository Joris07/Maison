from pymongo import MongoClient
from datetime import datetime
import paho.mqtt.subscribe as subscribe
import time

client = MongoClient('mongodb://127.0.0.1:27017') #Connexion à la base données
db = client["db"] #Pointe le nom de la base de données

#Interpréte les données reçu
def on_message_print(client, userdata, message):
    tropic= message.topic #Topic reçu
    data = message.payload.decode() #Valeur du topic reçu
    if((tropic + data)=="testtopictest message"): #Si la trame reçu est égal à 
        tropic = "AHT20/temperature" #tropic prend valeur 
        data = "20.52" #data prend valeur 
    print(tropic + data)
    tab = tropic.split("/") #Création d'un tableau en séparant les données par un "/"
    monDico= { } #Création du dictionnaire
    if(tab[1].find("temperature")!=-1): #Si la case contient "temperature" alors 
        monDico[tab[1]]=data #Remplit mon tableau de la valeur ex :{'temperature':'25'}
    elif(tab[1].find("humidite")!=-1): #Si la case contient "humidite" alors 
        monDico[tab[1]]=data #Remplit mon tableau de la valeur humidite ex : {'humidite':'20'}
    now = datetime.now()
    heure = now.strftime("%d/%m/%Y %H:%M:%S") #La variable heure prends pour valeur l'heure actuelle et la date
    monDico["date"] = heure                   #On ajoute l'heure et la date avec les variables température et humidite exemple {"humidite" : "50.47", "date" : "16/03/2021 13:13:14" }
    insert_bdd(tab[0][1:], monDico)           #Envoi des données dans la colonne passée en paramétre

#Insert les données dans la BDD
def insert_bdd(topic,dico):
    if(str(topic)=="AHT20"): #Si le topic est AHT20 alors
        col = db.AHT20 #Définit la colonne utilisée
        col.insert(dico) #Insert mes données dans la bdd
        client.close() #Termine l'envoi de données
    elif(str(topic)=="LM335"): #Si le topic est LMT335 alors
        col = db.LM335    #Définit la colonne utilisée
        col.insert(dico)  #Insert mes données dans la bdd
        client.close()    #Termine l'envoi de données

subscribe.callback(on_message_print, "#", hostname="172.20.78.137") #Souscrit à tous les topics "#", définit l'adresse du broker
