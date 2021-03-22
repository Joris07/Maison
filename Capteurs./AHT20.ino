#include <Adafruit_AHTX0.h>
#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3);

Adafruit_AHTX0 aht;
unsigned char count;

void setup() {


  pinMode(13, OUTPUT);      //On déclare le port 13 en sortie 
  digitalWrite(13, HIGH);   // On met le port 13 à 1 pour pouvoir alimenter le capteur
  xbee.begin(9600);         // On démarre la connexion en xbee à 9600 bauds
  Serial.begin(9600);
  Serial.println("Adafruit AHT10/AHT20 demo!");

  if (! aht.begin()) {                                  // Si on ne trouve pas le capteur 
    Serial.println("Could not find AHT? Check wiring");
    while (1) delay(10);
  }
  Serial.println("AHT10 or AHT20 found");
}

void loop() {
  sensors_event_t humidity, temp;      // Déclaration des valeurs qui contiennent les valeurs de l'humidité et de la température               
  aht.getEvent(&humidity, &temp);     // Permet d'avoir la dernière valeur de la température et de l'humidité

  String final = String(count) + "AHT20;t" + String(temp.temperature) + ";h" + String(humidity.relative_humidity);  // Envoi d'une trame "0AHT20;t20.20,h35;
  xbee.println(final);  //Envoi de la chaîne de caractère à l'autre module xbee
  count++;              //Variable qui permet de différencier 2 valeurs sucessives
  if (count == 2) count = 0;
  Serial.println(final);
  delay(30000);         //Delai de 30 secondes entre chaque valeurs pour ne pas surcharger la raspberry
}
