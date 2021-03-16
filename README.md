# Projet Maison Connectée
## Introduction
Le but du projet est de faire remonter les données de différents capteurs au sein d'une habitation et de les déposer dans une base de données. L'affichage est fait via une interface web. L'utilisateur souhaite avoir les données des différents capteurs situés dans sa maison en se connectant à l'interface web.

Exemple : 

![alt tag](https://github.com/Joris07/Maison/blob/main/maisonschema.PNG)

_Solutions techniques_ : Protocole Zigbee, Protocole MQTT, Serveur Flask, Utilisation d'une raspberry pi et d'une carte arduino, Base de données MongoDB.

_Languages_ : Arduino, Html, Javascript, Python, CSS.

## Présentation du projet
![alt tag](https://github.com/Joris07/Maison/blob/main/schemaprojet.png)
Comme on peut le voir sur le schéma le capteur AHT20 envoie une trame I2C à la carte  arduino et le capteur lm335 envoie une valeur analogique (la tension) qui sera convertit en valeur numérique sur la carte arduino pour pouvoir la traiter. Ensuite 2 cartes arduino communiquent grâce à des modules xbee avec la raspberry pi. La raspberry pi traite les valeurs des différents capteurs puis les envoient sur le broker mqtt grâce au script publish.py. Le serveur mqtt permet d'avoir différents topics auxquels on peut souscrire. Ensuite un script subscribe.py permet de soucscrire à tout les topics et envoie toutes les données reçues sur la base de données. On utilise MongoDB pour la base de données. Pour finir l'interface web intérragit avec la base de données pour avoir la dernière valeur enregistrée dans le base de données et une courbe en fonction du temps. 
