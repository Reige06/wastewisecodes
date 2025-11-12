
#include <WiFi.h>
#include <HTTPClient.h>
#include <ESP32Servo.h>

// -------------------- WiFi Setup --------------------
const char* ssid = "Infinix";
const char* password = "reige_123";

// -------------------- Backend Endpoint --------------------
const char* serverURL = "https://capstone-backend-3loo.onrender.com/api/bin-status/";

// -------------------- IR Sensor Pins --------------------
const int irBioPin = 4;   // Bio bin sensor
const int irRecyPin = 5;  // Recyclable bin sensor

// -------------------- Servo Setup --------------------
#define RX_PIN 3
#define SERVO_PIN 32

Servo myServo;

// -------------------- Tracking Variables --------------------
String lastBioStatus = "not full";
String lastNonBioStatus = "not full";

unsigned long bioStartTime = 0;
unsigned long recyStartTime = 0;
bool bioCounting = false;
bool recyCounting = false;

void setup() {
    Serial.begin(115200);
    Serial1.begin(115200, SERIAL_8N1, RX_PIN, -1);

    // Servo setup
    myServo.attach(SERVO_PIN);
    myServo.write(90);  // standby position
    Serial.println("ESP32 ready with Servo + IR sensors...");

    // Sensor setup
    pinMode(irBioPin, INPUT);
    pinMode(irRecyPin, INPUT);

    // WiFi setup
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi");
}

void loop() {
    // -------------------- IR Sensor Reading --------------------
    int bioSensorValue = digitalRead(irBioPin);
    int recySensorValue = digitalRead(irRecyPin);

    String bioStatus = "not full";
    String nonBioStatus = "not full";

    // ---- Bio Bin Logic ----
    if (bioSensorValue == LOW) {
        if (!bioCounting) {
            bioCounting = true;
            bioStartTime = millis();
        } else if (millis() - bioStartTime >= 5000) {
            bioStatus = "full";
        }
    } else {
        bioCounting = false;
    }

    // ---- Non-Bio Bin Logic ----
    if (nonBioSensorValue == LOW) {
        if (!nonBioCounting) {
            nonBioCounting = true;
            nonBioStartTime = millis();
        } else if (millis() - nonBioStartTime >= 5000) {
            nonBioStatus = "full";
        }
    } else {
        nonBioCounting = false;
    }

    // -------------------- Servo Control --------------------
    if (Serial1.available()) {
        String receivedLabel = Serial1.readStringUntil('\n'); 
        receivedLabel.trim();
        Serial.print("Received label: ");
        Serial.println(receivedLabel);

        // -------------------- Updated Decision --------------------
        if (receivedLabel.indexOf("Bio") >= 0 {
            
            if (bioStatus == "full") {
                Serial.println("⚠️ Bio bin is full. Garbage rejected.");
                myServo.write(90); // Stay locked
            } else {
                myServo.write(180);  // Bio side
                delay(1000);
                myServo.write(90);
                Serial.println("Bio garbage accepted.");
            }

        } else if (receivedLabel.indexOf("Non-bio") >= 0 {

            if (nonBioStatus == "full") {
                Serial.println("⚠️ Non-bio bin is full. Garbage rejected.");
                myServo.write(90);
            } else {
                myServo.write(0); // Recyclable side
                delay(1000);
                myServo.write(90);
                Serial.println("Non-bio garbage accepted.");
            }

        } else {
            Serial.println("Label not recognized. No movement.");
        }

        // ✅ Tell CAM it's safe to resume detection after handling
        Serial1.println("RESUME");
        Serial.println("Sent RESUME signal to CAM.");
    }

    // -------------------- Update Backend on Status Change --------------------
    if (bioStatus != lastBioStatus || nonBioStatus != lastNonBioStatus) {
        if (WiFi.status() == WL_CONNECTED) {
            HTTPClient http;
            http.begin(serverURL);
            http.addHeader("Content-Type", "application/json");

            String postData = "{\"bio_status\": \"" + bioStatus + 
                              "\", \"non_bio_status\": \"" + nonBioStatus + "\"}";

            int httpResponseCode = http.POST(postData);

            if (httpResponseCode > 0) {
                Serial.println("POST Success! Response: " + http.getString());
            } else {
                Serial.println("Error sending POST: " + String(httpResponseCode));
            }

            http.end();
        }

        lastBioStatus = bioStatus;
        lastNonBioStatus = nonBioStatus;
    }

    delay(200);
}




