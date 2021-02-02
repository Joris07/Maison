from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]
col = db.temperature

read = open("fichier.txt", "r")
lines = read.readlines()
read.close()
last_line = lines[len(lines)-1].strip()

doc = { "Temperature":last_line }

col.insert(doc)
client.close()
