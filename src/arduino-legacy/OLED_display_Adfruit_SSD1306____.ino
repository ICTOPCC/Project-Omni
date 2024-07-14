#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  // Initialize Serial Monitor for debugging
  Serial.begin(9600);

  // Initialize with the I2C address 0x3C (for 128x64)
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Infinite loop to stop further execution
  }

  // Clear the display buffer
  display.clearDisplay();
  
  // Display initial text
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Hello, World!");
  display.setCursor(0, 10);
  display.println("Arduino OLED Display");
  display.display();
}

void loop() {
  // Example variable to display
  static int counter = 0;

  // Clear the display buffer
  display.clearDisplay();

  // Set the text size and color
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  // Display the counter
  display.setCursor(0, 0);
  display.print("Counter: ");
  display.println(counter);

  // Update the display with the buffer content
  display.display();

  // Increment the counter
  counter++;

  // Delay for a bit (for demonstration purposes)
  delay(1000); // Update every second
}
