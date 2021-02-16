import serial
import time
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

ser = serial.Serial('/dev/ttyUSB0', 9600)

def receiver():
    incoming = ser.readline().strip()
    time.sleep(2)
    final= incoming[1:].decode()
    return final

def write_file(chaine):
    write = open("donnees.txt", "a")
    write.write(chaine[1:] + "\n")
    write.close()

def count_dot(chaine):
    nbr = chaine.count(';')
    return nbr

def trier(nbr, chaine):
    tab=chaine.split(";")
    memo = read_file().split(";")
    if(tab[0]!=memo[0]):
        monDico = { }
        for i in range(1, nbr+1):
            if(tab[i].find("t")!=-1):
                monDico["Temperature"] = tab[i][1:]
            elif(tab[i].find("h")!=-1):
                monDico["Humidite"] = tab[i][1:]
        insert_bdd(tab[0][1:], monDico)

def insert_bdd(topic,dico):
    if(str(topic[1:])=="AHT20"):
        col = db.AHT20
        col.insert(dico)
        client.close()
    elif(str(topic[1:])=="AHT10"):
        col = db.AHT10
        col.insert(dico)
        client.close()

def read_file():
    read = open("donnees.txt", "r")
    lines = read.readlines()
    read.close()
    last_line= lines[len(lines)-1].strip()
    return last_line

while 1:
    recu = receiver()
    trier(count_dot(recu), recu)
    write_file(recu)

