import serial
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

ser = serial.Serial('/dev/ttyUSB0', 9600)

def receiver():
    incoming = ser.readline().strip()
    final= incoming[1:].decode()
    print(final)
    return final

def write_file(chaine):
    write = open("donnees.txt", "a")
    write.write(chaine[1:] + "\n")
    write.close()

def count_dot(chaine):
    nbr = chaine.count(';')
    return nbr

'''def insert_bdd(nbr, chaine):
    tab=chaine.split(";")
    col = db.tab[0]
    for i=1 in range(nbr):'''
        
        
def read_file():
    read_temp = open("donnees.txt", "r")
    lines_temp = read_temp.readlines()
    read_temp.close()
    last_line= lines_temp[len(lines_temp)-1].strip()
    return last_line
    

def insert_aht20():

    doc = { "Temperature":last_line_temperature, "Humidite":last_line_humidity }

    col.insert(doc)
    client.close()

while 1:    
    receiver()
