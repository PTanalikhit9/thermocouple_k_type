#include <max6675.h>
#include <TimeLib.h>

// Sensor pins (from the first code)
int soPin = 4;
int csPin = 5;
int sckPin = 6;

MAX6675 robojax(sckPin, csPin, soPin);

void setup() {
  Serial.begin(9600);

  delay(900);
  Serial.println("CLEARSHEET"); // clears starting at row 1
  Serial.println("LABEL,Date,Time,Timeflow,Temperature(deg C)");
}

void loop() {
  // Use the TimeLib library functions to get date and time
  time_t t = now();
  String currentDate = String(year(t)) + "-" + String(month(t)) + "-" + String(day(t));
  String currentTime = String(hour(t)) + ":" + String(minute(t)) + ":" + String(second(t));

  // Construct the data string
  String dataString = "DATA," + currentDate + "," + currentTime + ",TIMER," + String(robojax.readCelsius());
  
  Serial.println(dataString);
  
  // Delay for 5 minutes (300,000 milliseconds)
  delay(300000);
}
