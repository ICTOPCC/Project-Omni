#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"

#define DHTPIN 2     // Define the pin where the data pin is connected
#define DHTTYPE DHT11   // Define the type of sensor
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
int time=0;
DHT dht(DHTPIN, DHTTYPE);

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// Example variable to display


void setup() {
  // Initialize Serial Monitor for debugging
  Serial.begin(9600);
  dht.begin();

  // Initialize with the I2C address 0x3C
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }

  // Clear the display buffer
  display.clearDisplay();

  // Display static text
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Value:");

  // Display the initial value of the variable
  display.setCursor(0, 10);
  // display.println(exampleVariable);

  // Display everything
  display.display();
  
  
}

void loop() {
  time++;
  // Reading temperature or humidity takes about 250 milliseconds!
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    display.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  // Clear the part of the display where the variable is shown
  display.fillRect(0, 10, 128, 10, SSD1306_BLACK);

  // Set the cursor to the position where the variable will be displayed
  display.setCursor(0, 10);
  

  // Print the updated value of the variable
  display.print("H:");
  display.println(h);
  display.print("T:");
  display.println(t);
  display.print("TI:");
  display.println(hic);
  display.print("Time Lapsed:");
  display.println(time);
  // Display everything
  display.display();
  display.clearDisplay();
  

  // Delay for a bit (for demonstration purposes)
  delay(1000);
}


