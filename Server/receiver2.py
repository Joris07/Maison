import serial
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

ser = serial.Serial('/dev/ttyUSB0', 9600)

def receiver():
    incoming = ser.readline().strip()
    final= incoming[1:].decode()
    return final

def write_file(chaine):
    write = open("donnees.txt", "a")
    write.write(chaine[1:] + "\n")
    write.close()

def count_dot(chaine):
    nbr = chaine.count(';')
    return nbr

def insert_bdd(nbr, chaine):
    tab=chaine.split(";")
    memo = read_file().split(";")
    if(tab[0]!=memo[0]):
        col = db.tab[0][1:]
        monDico = { }
        for i in range(1, nbr+1):
            if(tab[i].find("t")!=-1):
                monDico["Temperature"] = tab[i][1:]
            elif(tab[i].find("h")!=-1):
                monDico["Humidite"] = tab[i][1:]
        col.insert(monDico)
    client.close()

def read_file():
    read_temp = open("donnees.txt", "r")
    lines_temp = read_temp.readlines()
    read_temp.close()
    last_line= lines_temp[len(lines_temp)-1].strip()
    return last_line


recu = receiver()
write_file(recu)
insert_bdd(count_dot(recu), recu)
