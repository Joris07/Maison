import paho.mqtt.client as mqtt #import the client1
import serial
from pymongo import MongoClient
broker_address="172.20.78.137"
x=45 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("sensor/temperature",x)#publish
import serial
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client["db"]

ser = serial.Serial('/dev/ttyUSB0', 9600)

    
while 1:
    client = mqtt.Client("P1") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish("sensor/temperature",x)#publish
