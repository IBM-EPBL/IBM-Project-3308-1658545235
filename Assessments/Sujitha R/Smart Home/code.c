const int sensor = 2;
const int power = 3;
void setup()
{
  pinMode(power,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  long duration, cm;
  
  pinMode(sensor, OUTPUT);
  digitalWrite(sensor, LOW);
  delayMicroseconds(2);
  digitalWrite(sensor, HIGH);
  delayMicroseconds(5);
  digitalWrite(sensor, LOW);
  
  pinMode(sensor, INPUT);
  duration = pulseIn(sensor, HIGH);
  
  cm = microsecondsToCentimeters(duration);
  if(cm > 200){
    digitalWrite(power, HIGH);
  }
  else{
    digitalWrite(power, LOW);
  }
}
long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}
