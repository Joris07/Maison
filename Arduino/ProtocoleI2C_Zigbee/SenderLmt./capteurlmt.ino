/*
/*
 * Rui Santos
 * Complete Project Details https://RandomNerdTutorials.com
 */
 #include <Adafruit_AHTX0.h>
    #include <SoftwareSerial.h>
    SoftwareSerial xbee(2, 3);
     
 
const int sensorPin = A1; 
float sensorValue;
float voltageOut;

float temperatureC;
float temperatureF;
float temperatureK;

// uncomment if using LM335
//float temperatureK;
unsigned char count;

void setup() {
  pinMode(sensorPin, INPUT);
  xbee.begin(9600); 
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  voltageOut = (sensorValue * 5000) / 1024;
  
  // calculate temperature for LM35 (LM35DZ)
  //temperatureC = voltageOut / 10;
  //temperatureF = (temperatureC * 1.8) + 32;

  // calculate temperature for LM335
  temperatureK = voltageOut / 10;
  temperatureC = temperatureK - 273;
  //temperatureC=temperatureC/10;
  temperatureF = (temperatureC * 1.8) + 32;

  // calculate temperature for LM34
  //temperatureF = voltageOut / 10;
  //temperatureC = (temperatureF - 32.0)*(5.0/9.0);

//  Serial.print("Temperature(ºC): ");
//  Serial.print(temperatureC);
//  Serial.print("  Temperature(ºF): ");
//  Serial.print(temperatureF);
//  Serial.print("  Voltage(mV): ");
//  Serial.println(voltageOut);
//  Serial.println("Kelvin");
//  Serial.println(temperatureK);
  String final = String(count) + "LMT335;t" + String(temperatureC);
  count++;
      if (count==2) count=0; 
      Serial.println(final);
      xbee.println(final);
      delay(1000);
  delay(1000);
}
