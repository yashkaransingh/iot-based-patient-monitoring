#include <Wire.h>
#include "MAX30100_PulseOximeter.h"
 #include <ESP8266WiFi.h>
#include "ThingSpeak.h"
#define REPORTING_PERIOD_MS     1000
 
PulseOximeter pox;
uint32_t tsLastReport = 0;
WiFiClient client;
char ssid[] = "SSID";                                     // Your WiFi credentials.
char pass[] = "Password";
const unsigned long channel_id=your_channel_ID_of_thingspeak;
const char write_api_key[]="your channel write api key";
// Connections : SCL PIN - D1 , SDA PIN - D2 , INT PIN - D0
void onBeatDetected()
{
    Serial.println("Beat!");
}
 
void setup()
{
    Serial.begin(115200);
    Serial.print("Initializing pulse oximeter..");
 
    // Initialize the PulseOximeter instance
    // Failures are generally due to an improper I2C wiring, missing power supply
    // or wrong target chip
    if (!pox.begin()) {
        Serial.println("FAILED");
        for(;;);
    } else {
        Serial.println("SUCCESS");
    }
     pox.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);
 
    // Register a callback for the beat detection
    pox.setOnBeatDetectedCallback(onBeatDetected);
    WiFi.begin(ssid,password);
    while(WiFi.status()!=WL_CONNECTED){
  Serial.print(".");
  delay(500);
}
    ThingSpeak.begin(client);
randomSeed(micros());
}
 
void loop()
{
    // Make sure to call update as fast as possible
    pox.update();
    if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
     
        Heart_Rate = pox.getHeartRate();
        oxygen_level = pox.getSpO2();
        tsLastReport = millis();
        
    }
      ThingSpeak.setField(2,Heart_Rate);
 ThingSpeak.writeFields(channel_id,write_api_key);
  ThingSpeak.setField(1,oxygen_level);
 ThingSpeak.writeFields(channel_id,write_api_key);
    
}
