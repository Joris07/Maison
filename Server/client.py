import paho.mqtt.subscribe as subscribe

while 1:
    msg = subscribe.simple("sensor/temperature", hostname="172.20.78.137")
    print("%s %s" % (msg.topic, msg.payload.decode()))
