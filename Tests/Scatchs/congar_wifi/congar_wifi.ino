//https://github.com/dancol90/ESP8266Ping

#include <ESP8266WiFi.h>
#include "ESP8266Ping.h"
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Ultrasonic.h>

// rede, senha, ipservidor
const char* ssid = "ERROR";
const char* password =  "sword7991";
const IPAddress remote_ip(192, 168, 2, 103);
Ultrasonic ultrasonic1(D5, D6);

// mensagem
WiFiUDP Udp;
unsigned int localUdpPort = 5050;  // local port to listen on
char incomingPacket[255];  // buffer for incoming packets

void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);   
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");

  // udp porta
  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
 
}
 
void loop() {
  
  delay(300);
  digitalWrite(LED_BUILTIN, LOW);

  // enviar dados sensor
  Udp.beginPacket(remote_ip , localUdpPort );
  float x = 0.00;
  float z = ultrasonic1.distanceRead();
  
  
  Serial.print(z);
  Serial.print(" ");
  Serial.println(x);

  Udp.print(z);
  Udp.print(" ");
  Udp.println(x);
  Udp.endPacket();
  
}
  
