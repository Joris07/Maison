#include <Adafruit_Sensor.h>

#include <Adafruit_AHTX0.h>
#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3);


#include <Wire.h>
     
    Adafruit_AHTX0 aht;
    void Aht20 ();
    void InitAht20 ();
    void InitXbee ();
    void Xbee();
    
    void setup() {
       
       InitAht20(); 
       InitXbee ();
       
      
    }
     
    void loop() {
      Aht20 ();
      Xbee();
      
     
      delay(500);
    }
    void Aht20 (){

      unsigned char temperaturexbee,humiditexbee;
      sensors_event_t humidity, temp;  
      aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
      Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.println(" degrees C");
      Serial.print("Humidity: "); Serial.print(humidity.relative_humidity); Serial.println("% rH");
    }
    void InitAht20 (){
      Serial.begin(115200);
      Serial.println("Adafruit AHT10/AHT20 demo!");
     
      if (! aht.begin()) {
        Serial.println("Could not find AHT? Check wiring");
        while (1) delay(10);
      }
      Serial.println("AHT10 or AHT20 found");
      
    }
    void InitXbee (){
      
          xbee.begin(9600);                 
          Serial.begin(9600); 
    }
    void Xbee()
    {
      sensors_event_t humidity, temp; 
      Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.println(" degrees C");
      Serial.print("Humidity: "); Serial.print(humidity.relative_humidity); Serial.println("% rH");
      xbee.print(temp.temperature);
    }
    
