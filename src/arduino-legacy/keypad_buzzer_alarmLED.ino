#include <Keypad.h>

const byte ROWS = 4; // Four rows
const byte COLS = 3; // Three columns

// Define the keymap
char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

// Connect keypad ROW0, ROW1, ROW2, ROW3 to Arduino pins
byte rowPins[ROWS] = {9, 8, 7, 6};

// Connect keypad COL0, COL1, COL2 to Arduino pins
byte colPins[COLS] = {5, 4, 3};

// Create the Keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

const String passcode = "1234"; // Define the passcode
String enteredCode = ""; // Store the entered passcode
const int ledPin = 10; // LED pin for correct passcode
const int alertLedPin = 11; // LED pin for incorrect attempts
const int buzzerPin = 12; // Buzzer pin
const int doorOpen = 2;
int incorrectAttempts = 0; // Counter for incorrect attempts

void setup() {
  pinMode(ledPin, OUTPUT); // Set LED pin as output
  digitalWrite(ledPin, LOW); // Turn off the LED
  pinMode(alertLedPin, OUTPUT); // Set alert LED pin as output
  digitalWrite(alertLedPin, LOW); // Turn off the alert LED
  pinMode(buzzerPin, OUTPUT); // Set buzzer pin as output
  digitalWrite(buzzerPin, LOW); // Turn off the buzzer
  pinMode(doorOpen, OUTPUT);// To give the door opening signal
  digitalWrite(doorOpen,LOW);
  Serial.begin(9600); // Begin serial communication
}

void loop() {
  char key = keypad.getKey();

  if (key) {
    Serial.println(key);
    if (key == '#') {
      // Check the entered code
      if (enteredCode == passcode) {
        pinMode(ledPin, OUTPUT); // Set LED pin as output
        digitalWrite(ledPin, HIGH); // Turn on the LED if the passcode is correct
        digitalWrite(doorOpen,HIGH);// Open Door signal
        Serial.println("Correct passcode! Door opening!");
        delay(300); // Keep the LED on for 300 milliseconds
        digitalWrite(ledPin, LOW); // Turn off the LED
        digitalWrite(doorOpen,LOW); //End door signal
        incorrectAttempts = 0; // Reset the incorrect attempts counter
      } else {
        incorrectAttempts++; // Increment the incorrect attempts counter
        digitalWrite(ledPin, LOW); // Turn off the LED if the passcode is incorrect
        Serial.println("Incorrect passcode! LED is OFF.");
        if (incorrectAttempts >= 3) {
          digitalWrite(alertLedPin, HIGH); // Turn on the alert LED after 3 incorrect attempts
          digitalWrite(buzzerPin, HIGH); // Turn on the buzzer after 3 incorrect attempts
          Serial.println("Three consecutive incorrect attempts! Alert LED and Buzzer are ON.");
          delay(500); // Keep the alert LED and buzzer on for 3 seconds
          digitalWrite(alertLedPin, LOW); // Turn off the alert LED
          digitalWrite(buzzerPin, LOW); // Turn off the buzzer
          incorrectAttempts = 0; // Reset the incorrect attempts counter
          clearSerialMonitor(); // Clear the Serial Monitor
        }
      }
      enteredCode = ""; // Reset the entered code
    } else if (key == '*') {
      enteredCode = ""; // Clear the entered code if '*' is pressed
    } else {
      enteredCode += key; // Append the entered key to the passcode
    }
  }
}

// Function to clear the Serial Monitor
void clearSerialMonitor() {
  for (int i = 0; i < 50; i++) { // Adjust the number of lines as needed
    Serial.println();
  }
}




