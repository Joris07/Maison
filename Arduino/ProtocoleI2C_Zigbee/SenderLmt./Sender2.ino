    #include <SoftwareSerial.h>
    SoftwareSerial xbee(2, 3);
    
    unsigned char count;
     
    void setup() {
     
      pinMode(13, OUTPUT);
      digitalWrite(13, HIGH);
      xbee.begin(9600); 
      Serial.begin(9600);
      Serial.println("Adafruit AHT10/AHT20 demo!");
    }
      
    void loop() {

      String final = String(count) + "AHT10;t20.26;h38.16";
      xbee.println(final);
      count++;
      if (count==2) count=0; 
      Serial.println(final);
      delay(1000);
    }
