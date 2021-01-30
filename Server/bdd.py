from pymongo import MongoClient           

client = MongoClient("mongodb://127.0.0.1:27017)
db = myclient["db"]
collection = db.temperature

read = open("fichier.txt", "r")         '''Lire le fichier.txt'''
lines = read.readlines()
read.close()
last_line = lines[len(lines)-1].strip() '''Enregistre la derniére ligne en supprimant le saut de ligne'''

doc = { "Temperature":"19" }

collection.insert_one(doc)        '''Insert in the Database'''
client.close()
