import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:
    incoming = ser.readline().strip()
    final= incoming[1:].decode()

    f = open("fichier.txt", "a")
    f.write(final + "\n")
    f.close()

    print(final)
