#include <LiquidCrystal.h>


const int LM = A0;
const int motor = 13;



LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
 
  lcd.setCursor(3,0);
   lcd.print("Smart Home");
  pinMode(motor, OUTPUT);
  delay(2000);
  lcd.clear();
  lcd.print("Temp= ");
  lcd.setCursor(0,1);
  lcd.print("Pump= ");
}
void loop() {
  int value = analogRead(LM);
  float Temperature = value * 500.0 / 1023.0;
  lcd.setCursor(6,0);
  lcd.print(Temperature); 
  lcd.setCursor(11,1);
  

  if (Temperature > 50){
    digitalWrite(motor, HIGH);
    lcd.print("ON ");
  }
  else {
    digitalWrite(motor, LOW);
    lcd.print("OFF");
  }
  
   delay(1000);
}
