import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:
    incoming = ser.readline().strip()
    final= incoming[1:].decode()
    tab=final.split(";")
    temp=tab[0]
    humid=tab[1]
    f = open("fichier.txt", "a")
    f.write(temp + "\n" + humid + "\n")
    f.close()

    print(final)
