import paho.mqtt.client as mqtt #import the client1
from tkinter import *

#Get the window and set the size
window = Tk()
window.geometry('1000x100')
window.withdraw()

#Load both the images

label = Label(text="0", font="Arial 30", width=50, fg='red')#Initialise le label 
label.pack()

#Reçoit les données 
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))#Interprete la donnée reçu du topic
    salle= message.topic #Interprete le topic reçu
    tab=salle.split("/")#Sépare le topic au niveau du "/" en tableau
    print("message received " , float(msg))
    if(float(msg)>24):
        window.deiconify()#Fait apparaitre la fenêtre
        label.configure(text="ATTENTION IL FAIT %s°C DANS LA SALLE %s" % (msg,tab[0][1:]))#Remplace le message par le nouveau dans le label
        print("OK")
        label.update()#Met à jour le label
    else:
        window.withdraw()#Cache la fenêtre

broker_address="172.20.78.137"

print("creating new instance")
client = mqtt.Client() #Créer une nouvelle instance
client.on_message=on_message #Interprete le message en appelant la fonction on_message

print("connecting to broker")
client.connect(broker_address) #Connexion au broker

print("Subscribing to topic","AHT20/temperature")
client.subscribe("1AHT20/temperature")#Souscrit au topic 1AHT20/temperature

client.loop_start()#Démarre la boucle MQTT

window.mainloop()#Boucle lancant la fenêtre
