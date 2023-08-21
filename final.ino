#include <max6675.h>
#include <time.h>
#include <TimeLib.h>

int ktcSO = 4;
int ktcCS = 5;
int ktcCLK = 6;

#port 3
MAX6675 ktc(ktcCLK, ktcCS, ktcSO);

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
    +ktc.readCelsius() );
    
    //measuring time interval: changable
    delay(600);
}
