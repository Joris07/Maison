import serial
import time
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyUSB0', 9600)

broker_address="172.20.78.137"
client = mqtt.Client("P1")
client.connect(broker_address) #connect to broker

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

def trier(nbr, chaine):
    tab=chaine.split(";")
    memo = read_file().split(";")
    if(tab[0]!=memo[0]):
        for i in range(1, nbr+1):
            if(tab[i].find("t")!=-1):  
                client.publish("AHT20/temperature",tab[i][1:])#publish
            elif(tab[i].find("h")!=-1):
                client.publish("AHT20/humidite",tab[i][1:])#publish        

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
