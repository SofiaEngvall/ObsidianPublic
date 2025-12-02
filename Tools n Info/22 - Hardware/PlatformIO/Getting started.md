
ESP32 walkthrough example
https://docs.platformio.org/en/stable/tutorials/espressif32/arduino_debugging_unit_testing.html

```cpp
#include <Arduino.h>

// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  //int result = myFunction(2, 3);
  Serial.begin(9600);
  Serial.println("Serial.begin");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Some stuff...");
  delay(1000);
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}
```


other headers like wifi like:
`#include "wifi.h"`

