
#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3);
int count;
 
void setup()
{
    xbee.begin(9600);                 
    Serial.begin(9600);                     
    count = 0;
}
 
/***************************************
*  MAIN LOOP
***************************************/
 
void loop()
{
  String phrase = "Salut mon pote";
  
  Serial.println(phrase);
  xbee.println(phrase);
  
  delay(300);
}
