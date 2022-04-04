#include <Servo.h>

//Metronome Pins
#define metroLEDPin D10
#define metroBuzzPin D2
bool metroLEDState = false;
bool metroState = false;
float range = 300;

//Tambourine movement pins
#define xAxisPin D9
#define yAxisPin D8
//Tambourine 
Servo xAxis;
Servo yAxis;


//Tambourine percutor pins
#define percutorAPin D4
#define percutorBPin D6
#define percutorDPin D3
#define percutorIPin D7
#define percutorCPin D5
//Percutor 
Servo percutorA;
Servo percutorB;
Servo percutorD;
Servo percutorI;
Servo percutorC;


long lastTime = millis();
String inputMessage;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(3);
  calibrarMotores();

  pinMode(metroLEDPin,OUTPUT);
  pinMode(metroBuzzPin,OUTPUT);
}

void loop() {

  long elapsedTime = millis() - lastTime;
  lastTime = lastTime + elapsedTime;

  metronomo(elapsedTime,range);

  if(!Serial){
    Serial.end();
    delay(50);
    Serial.begin(115200);
  }else{
    inputMessage = Serial.readString();

    if(inputMessage == "1A"){
      abanico('A');

    }else if(inputMessage == "1B"){
      abanico('B');

    }else if(inputMessage == "2D"){
      vertical('D');

    }else if(inputMessage == "2I"){
      vertical('I');

    }else if(inputMessage == "3D"){
      percusionSimple(percutorD,percutorDPin);

    }else if(inputMessage == "3I"){
      percusionSimple(percutorI,percutorIPin);

    }else if(inputMessage == "3A"){
      percusionSimple(percutorA,percutorAPin);

    }else if(inputMessage == "3B"){
      percusionSimple(percutorB,percutorBPin);

    }else if(inputMessage == "3DI"){
      percusionDoble(percutorD,percutorDPin,percutorI,percutorIPin);

    }else if(inputMessage == "3AB"){
      percusionDoble(percutorA,percutorAPin,percutorB,percutorBPin);

    }else if(inputMessage == "4"){
      percusionSimple(percutorC,percutorCPin);

    }else if(inputMessage.startsWith("V")){
      String quanStr = "";
      for(int i = 1; i < inputMessage.length(); ++i){
        quanStr.concat(inputMessage[i]);
      }
      vibrato(quanStr.toInt());

    }else if(inputMessage.startsWith("MA")){
      String rangeStr = "";
      for(int i = 2; i < inputMessage.length(); ++i){
        rangeStr.concat(inputMessage[i]);
      }
      range = rangeStr.toFloat()/2*1000;
      metroState = true;

    }else if(inputMessage == "MD"){
      metroState = false;
    }

    delay(0.05);
    Serial.flush();
  }
}

void calibrarMotores(){
  int posInicial = 90;
  //Tambourine Movement motors
  xAxis.write(posInicial);
  yAxis.write(posInicial);
  xAxis.attach(xAxisPin);
  yAxis.attach(yAxisPin);

  //Percutors
  percutorA.write(posInicial);
  percutorB.write(posInicial);
  percutorD.write(posInicial);
  percutorI.write(posInicial);
  percutorC.write(posInicial);
  percutorA.attach(percutorAPin);
  percutorB.attach(percutorBPin);
  percutorD.attach(percutorDPin);
  percutorI.attach(percutorIPin);
  percutorC.attach(percutorCPin);

  delay(1000);
}

void metronomo(long eTime,float Range){
  if(metroState){
    static long metroTime = 0;
    metroTime = metroTime + eTime;

    if(metroTime >= Range){
      metroLEDState = !metroLEDState;
      digitalWrite(metroLEDPin,metroLEDState);
      metroTime = metroTime - Range;
    }
  }
}

void abanico(char Dir){
  xAxis.write(90);
  xAxis.attach(xAxisPin);
  if(Dir == 'A'){
    xAxis.write(180);
    delay(80);
    xAxis.write(90);
    delay(100);
  }else if (Dir == 'B'){
    xAxis.write(0);
    delay(80);
    xAxis.write(90);
    delay(100);
  }
  xAxis.write(90);
  delay(range-180);
  xAxis.detach();
}

void vertical(char Dir){
  yAxis.write(90);
  yAxis.attach(yAxisPin);
  if (Dir == 'D'){
    yAxis.write(180);
    delay(80);
    yAxis.write(90);
    delay(100);
  }else if (Dir == 'I'){
    yAxis.write(0);
    delay(80);
    yAxis.write(90);
    delay(100);
  }
  yAxis.write(90);
  delay(range-180);
  yAxis.detach();
} 

void vibrato(int quantity){
  int oldRange = range;
  range = 185;
  for(int i = 0; i < quantity; ++i){
    if(i%2 == 0){
      vertical('D');
    }else{
      vertical('I');
    }
  }
  range = oldRange;
}

void percusionSimple(Servo motor,uint8_t pin){
  motor.attach(pin);
  motor.write(-180);
  delay(80);
  motor.write(180);
  delay(78);
  /*
  motor.write(180);
  delay(25);*/
  //delay(range - 150);
  motor.detach();
}

void percusionDoble(Servo motor1, uint8_t pin1, Servo motor2, uint8_t pin2){
  motor1.attach(pin1);
  motor2.attach(pin2);
  motor1.write(90);
  motor2.write(90);
  delay(100);
  motor1.write(-90);
  motor2.write(-90);
  delay(range - 100);
  motor1.detach();
  motor2.detach();
}
