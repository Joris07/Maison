
   #include <Adafruit_AHTX0.h>
    #include <SoftwareSerial.h>
    SoftwareSerial xbee(2, 3);
     
    Adafruit_AHTX0 aht;
     
    void setup() {
      pinMode(13, OUTPUT);
      digitalWrite(13, HIGH);
      xbee.begin(9600); 
      Serial.begin(9600);
      Serial.println("Adafruit AHT10/AHT20 demo!");
     
      if (! aht.begin()) {
        Serial.println("Could not find AHT? Check wiring");
        while (1) delay(10);
      }
      Serial.println("AHT10 or AHT20 found");
    }
     
    void loop() {
      sensors_event_t humidity, temp;
      aht.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
      Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.println(" degrees C");
      Serial.print("Humidity: "); Serial.print(humidity.relative_humidity); Serial.println("% rH");
      xbee.print(temp.temperature);xbee.println(" degrees C");
      xbee.print(humidity.relative_humidity); xbee.println("% rH");
      delay(1500);
    }
