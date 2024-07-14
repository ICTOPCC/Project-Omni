#include <Servo.h>

// Define pins
const int button1Pin = 3; // Button 1 pin
const int button2Pin = 4; // signal from PIN Nano
const int ledPin = 8;     // LED pin
const int irSensorPin1 =9 ; // IR sensor pin 1
const int irSensorPin2 =10 ; // IR sensor pin 2
const int servoPin = 11;   // Servo pin

// Create a Servo object
Servo myServo;

void setup() {
  // Initialize the button pins as input
  //pinMode(button1Pin, INPUT);
  Serial.begin(9600);
  pinMode(button2Pin, INPUT);

  // Initialize the LED pin as output
  pinMode(ledPin, OUTPUT);

  // Initialize the IR sensor pin as input
  pinMode(irSensorPin2, INPUT);

  // Attach the servo to the servo pin
  myServo.attach(servoPin);

  // Start the servo at 0 degrees
  myServo.write(0);
}

void loop() {
  // Read the state of the push buttons
  int button1State = digitalRead(button1Pin);
  int button2State = digitalRead(button2Pin);

  // If either button is pressed, move the servo to 90 degrees
  if (button2State == HIGH ||button1State== HIGH ) {
    myServo.write(90);
    digitalWrite(ledPin, HIGH); // Turn on the LED
    delay(1000); // Debounce delay to avoid multiple activations

    // Stay in this position as long as the IR sensor detects an obstacle
    while (digitalRead(irSensorPin2) == LOW|| digitalRead(irSensorPin1) == LOW ) {
      Serial.println(digitalRead(button2Pin));
      delay(2000); // Check every 2 seconds
      
    }

    // Once no obstacle is detected, wait for 1 second
    delay(1000);

    // Return the servo to 0 degrees
    myServo.write(0);
    delay(2000);
    digitalWrite(ledPin, LOW); // Turn off the LED
  }

  delay(100); // Small delay to avoid excessive processing
}

