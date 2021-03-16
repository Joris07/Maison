import serial
import time
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyUSB0', 9600) #Déclaration du port série et de sa fréquence 

broker_address="172.20.78.137" #Déclaration de l'adresse du broker
client = mqtt.Client("P1") #Instancie un client
client.connect(broker_address) #connect to broker

#Retourne la trame reçu sur le xbee
def receiver():
    incoming = ser.readline().strip() #Lecture du port série en supprimant les espaces
    final= incoming[1:].decode() #Decode la trame reçu encoder 
    return final #Retourne la trame

#Ecrit la trame xbee dans le fichier txt
def write_file(chaine):
    write = open("donnees.txt", "a") #Ouvre le fichier "donnees.txt" pour écrire dedans ("a")
    write.write(chaine[1:] + "\n") #Ecrit dans le fichier + saut de ligne
    write.close() #Ferme le fichier

#Compte le nombre de ; dans la trame xbee
def count_dot(chaine):
    nbr = chaine.count(';') #Compte le nombre de point virgule dans la chaîne de caractéres
    return nbr #Retourne le nombre de point virgule

#Trie la trame et publie les données sur le broker 
def trier(nbr, chaine):
    tab=chaine.split(";") #Création d'un tableau en séparant les données par un ;
    memo = read_file().split(";") #Récupération de la derniére valeur publiée
    if(tab[0]!=memo[0]): #Si la valeur reçu est différente de la derniére publiée alors
        for i in range(1, nbr+1): #Parcours toutes les cases du tableau en commencant à la 2éme
            if(tab[i].find("t")!=-1): #Si la case contient un t alors  
                client.publish(tab[0][1:]+"/temperature",tab[i][1:]) #Publie la temperature du topic sur le broker 
            elif(tab[i].find("h")!=-1): #Si la case contient un h alors
                client.publish(tab[0][1:]+"/humidite",tab[i][1:]) #Publie l'humidité du topic sur le broker       

#Lecture de la derniére ligne du fichier txt
def read_file():
    read = open("donnees.txt", "r") #Ouvre le fichier donnees.txt en lisant (r)
    lines = read.readlines() #Lis le contenu du fichier
    read.close() #Ferme le fichier
    last_line= lines[len(lines)-1].strip() #Récupére la derniére ligne
    return last_line #Retourne la derniére ligne du fichier

#Faire sans cesse
while 1:
    recu = receiver()
    print(recu)
    trier(count_dot(recu), recu)
    write_file(recu)
