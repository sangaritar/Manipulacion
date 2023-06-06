int EnA=10;
int EnB=11;
int inA1=6;
int inA2=7;
int inB1=8;
int inB2=9;
int En1A=5;
int En1B=5;

void setup() {
   Serial.begin(9600);
}



void loop() {
  imprimir();
  if (Serial.available()) {
    char c = Serial.read();
    switch(c) {
      case 'w':
        moveForward();
        break;
      case 's':
        moveBackward();
        break;
      case 'a':
        turnLeft();
        break;
      case 'd':
        turnRight();
        break;
      case 'q':
        stopMotors();
        break;
    }
  }
}

void moveForward() {
  analogWrite(EnA,255); 
  analogWrite(EnB,255);
  digitalWrite(inA1, HIGH);
  digitalWrite(inA2, LOW);
  digitalWrite(inB1, HIGH);
  digitalWrite(inB2, LOW);
}

void moveBackward() {
  analogWrite(EnA,255); 
  analogWrite(EnB,255);
  digitalWrite(inA1, LOW);
  digitalWrite(inA2, HIGH);
  digitalWrite(inB1, LOW);
  digitalWrite(inB2, HIGH);
}

void turnLeft() {
  analogWrite(EnA,255); 
  analogWrite(EnB,255);
  digitalWrite(inA1, LOW);
  digitalWrite(inA2, HIGH);
  digitalWrite(inB1, HIGH);
  digitalWrite(inB2, LOW);
}
void turnRight() {
  analogWrite(EnA,255); 
  analogWrite(EnB,255);
  digitalWrite(inA1, HIGH);
  digitalWrite(inA2, LOW);
  digitalWrite(inB1, LOW);
  digitalWrite(inB2, HIGH);
}

void stopMotors() {
  analogWrite(EnA,0); 
  analogWrite(EnB,0);
  digitalWrite(inA1, LOW);
  digitalWrite(inA2, LOW);
  digitalWrite(inB1, LOW);
  digitalWrite(inB2, LOW);
}
void imprimir(){
  int a=digitalRead(En1A);
  int b=digitalRead(En1B);
  Serial.print(a*5);
  Serial.print(" ");
  Serial.println(b*5);
}
