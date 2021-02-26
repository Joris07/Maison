from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017') #Connexion à la base données
db = client["db"] #Pointe le nom de la base de données
todos = db.AHT20 #Select the collection name

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/action", methods=['POST'])    
def action ():       
    recu=request.values.get("name")       
    print(recu)
    todos_l = todos.find({ "humidite": {"$gt":"20"}})
    print(todos_l)
    return render_template('index.html',recu=recu, todos=todos_l)
