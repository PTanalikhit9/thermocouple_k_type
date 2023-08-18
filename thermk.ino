 // original library source:
// www.ladyada.net/learn/sensors/thermocouple
 /*
 * Arduino code to read temperature using MAX6675 chip and k-type thermocouple
 * and display it on serial monitor
 * 
 * Watch video instruction for this code: https://youtu.be/VGqONmUinqA
 * Download this code from Robojax.com
 *  
 * updated by Ahmad Shamshiri for Robojax.com on Saturday November 23, 2018 
 * at 21:25 in Ajax, Ontario, Canada
 * 
 
 * This code is "AS IS" without warranty or liability. Free to be used as long as you keep this note intact.* 
 * This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

 
#include "max6675.h" // max6675.h file is part of the library that you should download from Robojax.com

int soPin = 4;// SO=Serial Out
int csPin = 5;// CS = chip select CS pin
int sckPin = 6;// SCK = Serial Clock pin

MAX6675 robojax(sckPin, csPin, soPin);// create instance object of MAX6675


void setup() {

          
  Serial.begin(9600);// initialize serial monitor with 9600 baud
  Serial.println("Robojax MAX6675"); 

}

void loop() {
  // basic readout test, just print the current temp
  // Robojax.com MAX6675 Temperature reading on Serial monitor
   Serial.print("C = "); 
   Serial.print(robojax.readCelsius());
   Serial.print(" F = ");
   Serial.println(robojax.readFahrenheit());

             
   delay(1000);
}
