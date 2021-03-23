
#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3);
     
 
const int sensorPin = A1; 
float sensorValue;
float voltageOut;

float temperatureC;
float temperatureK;


unsigned char count;

void setup() {
  pinMode(sensorPin, INPUT);
  xbee.begin(9600);           //On démarre la connexion xbee avec une vitesse de 9600 bauds
  Serial.begin(9600);
  pinMode(13, OUTPUT);        //On configure le port 13 en sortie 
  digitalWrite(13, HIGH);     // On écrit un niveau logique haut sur le port 13 pour pouvoir alimenter le capteur. 
}

void loop() {
  sensorValue = analogRead(sensorPin);
  voltageOut = (sensorValue * 5000) / 1024; //Conversion numérique analogique pour avoir la tension en sortie du capteur
  temperatureK = voltageOut / 10;           // On divise par 10 pour avoir la tension en mv
  temperatureC = temperatureK - 273;        // On convertit la température en kelvin en degré
  String final = String(count) + "LMT335;t" + String(temperatureC);
  count++;
      if (count==2) count=0; // Variable pour différencier 2 valeurs sucessives
      Serial.println(final);  
      xbee.println(final);  // On envoie la chaîne de caractères "final"
      delay(30000);         // On met un délai de 30 secondes pour pas surcharger le broker sur la raspberry 
  
}
