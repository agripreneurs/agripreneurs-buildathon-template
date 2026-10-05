/*
  Agripreneurs Buildathon - Hardware Firmware Starter
  Target Board: ESP32 Dev Module / Arduino
  Description: Reads analog capacitive soil moisture sensor and triggers irrigation relay.
*/

// Pin Assignments
const int PIN_SOIL_MOISTURE = 34; // ADC1 channel on ESP32
const int PIN_RELAY_VALVE   = 23; // Digital output to relay
const int PIN_STATUS_LED    = 2;  // Onboard LED

// Calibration Constants (Calibrate in dry air vs cup of water)
const int DRY_SENSOR_VAL  = 3200; // Typical 12-bit ADC reading in air
const int WET_SENSOR_VAL  = 1400; // Typical reading submerged in water
const float MOISTURE_THRESHOLD_PCT = 25.0; // Trigger threshold

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("==========================================");
  Serial.println("🌾 Agripreneurs Buildathon - IoT Node Boot");
  Serial.println("==========================================");

  pinMode(PIN_RELAY_VALVE, OUTPUT);
  pinMode(PIN_STATUS_LED, OUTPUT);
  digitalWrite(PIN_RELAY_VALVE, LOW); // Default OFF
}

float readSoilMoisturePercent() {
  int rawVal = analogRead(PIN_SOIL_MOISTURE);
  // Map raw reading to 0 - 100% moisture
  float moisturePct = map(rawVal, DRY_SENSOR_VAL, WET_SENSOR_VAL, 0, 100);
  return constrain(moisturePct, 0.0, 100.0);
}

void loop() {
  float moisture = readSoilMoisturePercent();
  Serial.print("Soil Moisture: ");
  Serial.print(moisture);
  Serial.print("% | Valve: ");

  if (moisture < MOISTURE_THRESHOLD_PCT) {
    digitalWrite(PIN_RELAY_VALVE, HIGH); // Turn ON valve
    digitalWrite(PIN_STATUS_LED, HIGH);
    Serial.println("ACTIVE (Irrigating)");
  } else {
    digitalWrite(PIN_RELAY_VALVE, LOW);  // Turn OFF valve
    digitalWrite(PIN_STATUS_LED, LOW);
    Serial.println("IDLE (Moisture Adequate)");
  }

  // Sample every 5 seconds (in production, use deep sleep or longer intervals)
  delay(5000);
}
