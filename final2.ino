#include <max6675.h>
#include <time.h>
#include <TimeLib.h>

int ktcSO = 4;
int ktcCS = 5;
int ktcCLK = 6;

int ktcSO2 = 7;
int ktcCS2 = 8;
int ktcCLK2 = 9;

MAX6675 ktc(ktcCLK, ktcCS, ktcSO);
MAX6675 ktc2(ktcCLK2, ktcCS2, ktcSO2);

int i = 0;

void setup() {
  // open serial connection

  Serial.begin(9600);
  // give the MAX a little time to settle
  delay(900);
  Serial.println("CLEARSHEET"); // clears starting at row 1
  Serial.println("LABEL, Date, Time, Timeflow, Inside Temp (deg C), Outside Temp(deg C)");
}

void loop() {
    Serial.println( (String) "DATA,DATE,TIME,TIMER,"
    +ktc.readCelsius()+","+ktc2.readCelsius() );
    
    //measuring time interval: changable
    delay(60000);
}
