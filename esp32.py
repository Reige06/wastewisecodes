#include <ESP32Servo.h>

#define RX_PIN 3      // GPIO 3 (RX) for Serial1
#define SERVO_PIN 5   // Replace with the pin connected to your SG92R signal wire

Servo myServo;

void setup() {
    Serial.begin(115200);      // Initialize Serial Monitor
    Serial1.begin(115200, SERIAL_8N1, RX_PIN, -1);  // UART RX on GPIO 3

    myServo.attach(SERVO_PIN);  // Attach servo to the specified pin
    myServo.write(90);          // Start at 90 degrees
    Serial.println("Receiver ESP32 is ready to receive predictions...");
}

void loop() {
    if (Serial1.available()) {
        String receivedLabel = Serial1.readStringUntil('\n'); 
        Serial.print("Received label: ");
        Serial.println(receivedLabel);

        

        // Match against lowercase keywords
        if (receivedLabel.indexOf("paper-bowl") >= 0) {
            myServo.write(0);
        }else if (receivedLabel.indexOf("spoon") >= 0) {
            myServo.write(0);
        } else if (receivedLabel.indexOf("plastic-bottle") >= 0) {
            myServo.write(180);
        } else {
            Serial.println("Label not recognized. No movement.");
        }

          // Allow time for servo movement
        delay(2000);
        myServo.write(90);  // Return to standby
        Serial.println("Returned to 90° (standby)");

    

        
    }
}

