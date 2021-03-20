from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017') #Connexion à la base données
db = client["db"] #Pointe le nom de la base de données

app = Flask(__name__)

#Récupére la derniére valeur de temperature dans la collection AHT20
def lastValueTemperatrue():
    temperature_1 = db.AHT20.find().sort("temperature", -1).limit(1)
    for x in temperature_1:
        return x

#Récupére la derniére valeur d'humidité' dans la collection AHT20
def lastValuehumidity():
    humidite_1= db.AHT20.find().sort("humidite", -1).limit(1)
    for x in humidite_1:
        return x

#Récupére la derniére valeur de temperature dans la collection LM335
def lastValuelm335 ():
    lm335_1= db.LM335.find().sort("temperature", -1).limit(1)
    for x in lm335_1:
        return x

#Récupére les collections contenu dans la base de données "bd"
def collection():
    coll = db.collection_names()
    coll.remove("system.indexes")
    coll.remove('tab.0.slice(1, None, None)')
    coll.remove('topic.slice(1, None, None)')
    return coll

#Récupére l'humidité et la date de la collection AHT20 en les stockants dans des tableaux
def stock_humidity_AHT20():
    data = db.AHT20.find({ "humidite": {"$gt":"#"}})
    date=[]
    humidity=[]
    for i in data:
        date.append(i.get("date"))
        humidity.append(i.get("humidite"))
    return (humidity,date)

#Récupére la température et la date de la collection AHT20 en les stockants dans des tableaux
def stock_temp_AHT20():
    data = db.AHT20.find({ "temperature": {"$gt":"#"}})
    date=[]
    temp=[]
    for i in data:
        date.append(i.get("date"))
        temp.append(i.get("temperature"))    
    return (temp,date)

#Récupére la température et la date de la collection LM335 en les stockants dans des tableaux
def stocklm335():
    data=db.LM335.find({ "temperature": {"$gt":"#"}})#Récupére toutes les données de température
    lm335=[]
    datelm335=[]
    for i in data:
        datelm335.append(i.get("date"))
        lm335.append(i.get("temperature"))
    return (lm335,datelm335)

#Transmet les valeurs de la bdd vers l'index.html en fonction des listes déroulantes
@app.route("/")
def index():
    topic=request.values.get("topic")
    capteur=request.values.get("capteur")
    coll = collection()
    if(topic=="AHT20" and capteur=="Temperature"):#Si le choix de topic est AHT20 et le capteur est temperature alors
        temp,date=stock_temp_AHT20()
        temperature=lastValueTemperatrue().get("temperature")
        humidite=0
    elif(topic=="AHT20" and capteur=="Humidite"):#Si le choix de topic est AHT20 et le capteur est humidite alors
        temp,date=stock_humidity_AHT20()
        humidite=lastValuehumidity().get('humidite')
        temperature = 0
    elif(topic=="LM335" and capteur=="Temperature"):#...
        temp,date=stocklm335()
        temperature=lastValuelm335().get('temperature')
        humidite=0
    elif(topic=="AHT20" and capteur=="#"):#...
        temp,date=stocklm335()
        temperature=lastValuelm335().get('temperature')
        humidite= lastValuehumidity().get('humidite')
    else:#Sinon la valeur par défaut sera de 0
        temp,date=0,0
        temperature = 0
        humidite = 0
    return render_template('index.html', temperature=temperature, humidite=humidite, coll=coll, temp=temp, date=date)#Envoi des données sur l'index

#Démarre le serveur
if __name__ == "__main__":
    app.run(debug=True)

