#include <max6675.h>
#include <time.h>
#include <TimeLib.h>

int ktcSO = 8;
int ktcCS = 9;
int ktcCLK = 10;
int ktcSO2 = 5;
int ktcCS2 = 6;
int ktcCLK2 = 7;

MAX6675 ktc(ktcCLK, ktcCS, ktcSO);
MAX6675 ktc2(ktcCLK2, ktcCS2, ktcSO2);

int i = 0;

void setup() {
  // open serial connection

  Serial.begin(9600);
  // give the MAX a little time to settle
  delay(900);
  Serial.println("CLEARSHEET"); // clears starting at row 1
  Serial.println("LABEL, Date, Time, Timeflow, Angle Valve(deg C), Gate Valve(deg C)");
}

void loop() {
    Serial.println( (String) "DATA,DATE,TIME,TIMER,"
    +ktc.readCelsius()+","+ktc2.readCelsius() );
    
    //measuring time interval: changable
    delay(300000);
}
