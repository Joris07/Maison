    #include <Adafruit_AHTX0.h>
    #include <SoftwareSerial.h>
    SoftwareSerial xbee(2, 3);
     
    Adafruit_AHTX0 aht;
    unsigned char count;
     
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
 
      String final = String(count) + "AHT20;t" + String(temp.temperature) + ";h" + String(humidity.relative_humidity);
      xbee.println(final);
      count++;
      if (count==2) count=0; 
      Serial.println(final);
      delay(1000);
    }
