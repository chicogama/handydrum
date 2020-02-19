#include <Ultrasonic.h> // Declaração de biblioteca
 
Ultrasonic ultrasonic1(D0, D1); // Instância chamada ultrasonic com parâmetros (trig,echo)
Ultrasonic ultrasonic2(D5, D6);

 
void setup() { 
  Serial.begin(115200); // Inicio da comunicação serial
}
 
void loop() { 
  Serial.print("Distancia: "); // Escreve texto na tela
  Serial.println("");
  Serial.println(ultrasonic1.distanceRead());// distância medida em cm
  Serial.println("cm"); // escreve texto na tela e pula uma linha
  Serial.print(ultrasonic2.distanceRead());// distância medida em cm
  Serial.println("cm"); // escreve texto na tela e pula uma linha
  delay(100); // aguarda 1s 
}
