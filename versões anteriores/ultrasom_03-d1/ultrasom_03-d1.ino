//Trig - output
#define trigPin1 D8
// D8 - D8
//Echo - input
#define echoPin1 D6
// D6 - D12

// D5 - D5;  D2 - D2
#define trigPin2 D5
#define echoPin2 D2

double duration_1, duration_2, cm_1, cm_2;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Definicao de portas
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
}
 
void loop() {
  
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite( trigPin1, LOW );
  delayMicroseconds( 2 );
  digitalWrite( trigPin1, HIGH );  // envia um sinal por 10 ms
  delayMicroseconds( 5 );
  digitalWrite( trigPin1, LOW );   // para o sinal 
  delayMicroseconds( 5 );  
 
  // echoPin ler um sinal de pulso HIGH
  // pulseIn retorna em microsegundos
  // 
  //pinMode(echoPin, INPUT);
  duration_1 = pulseIn( echoPin1, HIGH );    

  digitalWrite( trigPin2, LOW );
  delayMicroseconds( 2 );
  digitalWrite( trigPin2, HIGH );  // envia um sinal por 10 ms
  delayMicroseconds( 5 );
  digitalWrite( trigPin2, LOW );   // para o sinal 
  delayMicroseconds( 5 );

  duration_2 = pulseIn( echoPin2, HIGH );
   
  // convert tempo para distancia
  cm_1 = ( duration_1/2 ) / 58.1;
  cm_2 = ( duration_2/2 ) / 58.1;
  //Serial.print( duration );
  //Serial.print( " 1 " );
  Serial.print( cm_1 );
  Serial.print( " " );
  Serial.println( cm_2 );
  
  //if( cm < 5.00 ){
  //  Serial.println( "Pare" );
  //}

  //if( cm > 30.00 ){
  //  Serial.println( "Ande" );
  //}
  
  delay(20);
}
