import serial
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

ser = serial.Serial('/dev/ttyUSB0', 9600)

def receiver_xbee1():
    incoming = ser.readline().strip()
    final= incoming[1:].decode()
    
    tab=final.split(";")
    temp=tab[0]
    humid=tab[1]

    read_temperature = open("temperature.txt", "a")
    read_temperature.write(temp)
    read_temperature.close()

    read_humidity = open("humidite.txt", "a")
    read_humidity.write(humid)
    read_humidity.close()

def insert_aht20():
    col = db.aht20

    read_temp = open("temperature.txt", "r")
    lines_temp = read_temp.readlines()
    read_temp.close()
    last_line_temperature = lines_temp[len(lines_temp)-1].strip()

    read_humid = open("humidite.txt", "r")
    lines_humid = read_humid.readlines()
    read_humid.close()
    last_line_humidity = lines_humid[len(lines_humid)-1].strip()

    doc = { "Temperature":last_line_temperature, "Humidite":last_line_humidity }

    col.insert(doc)
    client.close()

while 1:
    receiver_xbee1()
