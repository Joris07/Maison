

#MongoDB shell version Installation

sudo apt install mongodb

sudo systemctl enable mongodb

###Accéder à la base 

mongo

###Utiliser la base de données

use db

###Créer une collection

db.createCollection("name")

###Afficher les données d'une collection 

db.collection.find()

###Ajouter des données à une collection 

db.collection.insert({a:2})

###Supprimer une collection 

db.drop("collection")

###Supprimer des données d'une collection 

db.collection.remove({a:2})

###Pour plus de commande suivre ce lien 

https://docs.mongodb.com/manual/reference/method/js-collection/
