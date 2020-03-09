#include <ESP8266WiFi.h>
#include "ESP8266Ping.h"
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Ultrasonic.h>
#include <PubSubClient.h>

// rede, senha, ipservidor
const char* ssid = "LABRTL-22426";
const char* password =  "7gPBsaUF";
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
const IPAddress remote_ip(10, 42, 0, 170);
Ultrasonic ultrasonic1(D1, D2);
Ultrasonic ultrasonic2(D6, D5);

//Inicializando MQTT
void subscribeReceive(char* topic, byte* payload, unsigned int length);
const char* server = "test.mosquitto.org";

//Variáveis pra manipulação dos dados
char dis1[6];
char dis2[6];
char buf[10];
String temp;
String humi;
String temphumi;

WiFiClient espClient;
PubSubClient mqttClient(espClient);

// mensagem
WiFiUDP Udp;
unsigned int localUdpPort = 5050;  // local port to listen on
char incomingPacket[255];  // buffer for incoming packets


void setup() {
  // put your setup code here, to run once:

  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);   
    Serial.println("Connecting to WiFi.."); 
  }
 
  Serial.println("Connected to the WiFi network");

  // udp porta
  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

   mqttClient.setServer(server, 1883);   
 
  // Attempt to connect to the server with the ID "myClientID"
  if (mqttClient.connect("1")) 
  { 
    Serial.println("Connection has been established, well done");
 
    // Establish the subscribe event
    mqttClient.setCallback(subscribeReceive);
  } 
  else 
  {
    Serial.println("Looks like the server connection failed...");
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:
    delay(300);
  digitalWrite(LED_BUILTIN, LOW);

  // enviar dados sensor
  Udp.beginPacket(remote_ip , localUdpPort );
  float x = ultrasonic1.distanceRead();
  float z = ultrasonic2.distanceRead();

  Serial.print("1");
  Serial.print(" ");
  Serial.print(z);
  Serial.print(" ");
  Serial.println(x);

  Udp.print("1");
  Udp.print(" ");
  Udp.print(z);
  Udp.print(" ");
  Udp.println(x);
  Udp.endPacket();
  mqttClient.loop();

  dtostrf(x,3,1,dis1);
  dtostrf(z,3,1,dis2);

  temp = dis2;
  humi = dis1;
  temphumi = "1 "+ temp+" "+humi;
  temphumi.toCharArray(buf, 15);
 
  // Ensure that we are subscribed to the topic "MakerIOTopic"
  mqttClient.subscribe("tempmonitor");
   if(mqttClient.publish("tempmonitor", buf))
  {
    Serial.println("Publish message success");
  }
  else
  {
    Serial.println("Could not send message :(");
  }
 
  // Dont overload the server!
  delay(300);
}
void subscribeReceive(char* topic, byte* payload, unsigned int length)
{
  // Print the topic
  Serial.print("Topic: ");
  Serial.println(topic);
 
  // Print the message
  Serial.print("Message: ");
  for(int i = 0; i < length; i ++)
  {
    Serial.print(char(payload[i]));
  }
 
  // Print a newline
  Serial.println("");

}
