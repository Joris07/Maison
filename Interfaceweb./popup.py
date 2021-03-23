import paho.mqtt.client as mqtt #import the client1
from tkinter import *

#Get the window and set the size
window = Tk()
window.geometry('150x50')

#Load both the images

label = Label(text="0", font="Arial 30", width=10)#Initialise le label 
label.pack()

#Reçoit les données 
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))#Interprete le message recu du topic
    print("message received " , msg)
    label.configure(text="%s" % msg)#Remplace le message par le nouveau dans le label
    print("OK")
    label.update()#Met à jour le label 

broker_address="172.20.78.137"

print("creating new instance")
client = mqtt.Client() #Créer une nouvelle instance
client.on_message=on_message #

print("connecting to broker")
client.connect(broker_address) #Connexion au broker

print("Subscribing to topic","AHT20/temperature")
client.subscribe("1AHT20/temperature")#Souscrit au topic 1AHT20/temperature

client.loop_start()#Démarre la boucle MQTT

window.mainloop()
