import paho.mqtt.client as mqtt #import the client1
from tkinter import *

#Get the window and set the size
window = Tk()
window.geometry('150x50')

#Load both the images

label = Label(text="0", font="Arial 30", width=10)
label.pack()

# This is the event handler method that receives the Mosquito messages
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received " , msg)
    label.configure(text="%s" % msg)
    print("OK")
    label.update()

broker_address="172.20.78.137"

print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Subscribing to topic","AHT20/temperature")
client.subscribe("1AHT20/temperature")

 #Start the MQTT Mosquito process loop
client.loop_start() 

window.mainloop()
