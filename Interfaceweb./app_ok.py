from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017') #Connexion à la base données
db = client["db"] #Pointe le nom de la base de données

app = Flask(__name__)

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

def collection():
    coll = db.collection_names()
    coll.remove("system.indexes")
    coll.remove('tab.0.slice(1, None, None)')
    coll.remove('topic.slice(1, None, None)')
    return coll

def stock_humidity_AHT20():
    data = db.AHT20.find({ "humidite": {"$gt":"#"}})
    date=[]
    humidity=[]
    for i in data:
        date.append(i.get("date"))
        humidity.append(i.get("humidite"))
     
    return (humidity,date)

def stock_temp_AHT20():
    data = db.AHT20.find({ "temperature": {"$gt":"#"}})
    date=[]
    temp=[]
    for i in data:
        date.append(i.get("date"))
        temp.append(i.get("temperature"))
    date.remove(None)    
    return (temp,date)

def stocklmt335():
    data=db.LMT335.find({ "temperature": {"$gt":"#"}})
    lmt335=[]
    datelmt335=[]
    for i in data:
        datelmt335.append(i.get("date"))
        lmt335.append(i.get("temperature"))
    return (lmt335,datelmt335)


@app.route("/")
def index():
    temperature=lastValueTemperatrue().get("temperature")
    topic=request.values.get("topic")
    capteur=request.values.get("capteur")
    humidite=lastValuehumidity().get('humidite')
    lmt335=lastValuelm335().get('temperature')
    coll = collection()
    if(topic=="AHT20" and capteur=="Temperature"):
        temp,date=stock_temp_AHT20()
    elif(topic=="AHT20" and capteur=="Humidite"):
        temp,date=stock_humidity_AHT20()
    elif(topic=="LMT335" and capteur=="Temperature"):
        temp,date=stocklmt335()
    else: 
        temp,date=stock_temp_AHT20()
    return render_template('index.html', temperature = temperature, humidite = humidite, lmt335=lmt335, coll=coll, temp=temp,date=date)

if __name__ == "__main__":
    app.run(debug=True)
