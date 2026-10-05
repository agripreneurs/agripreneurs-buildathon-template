# Hardware Documentation (`/hardware`)

*If your solution includes physical computing, IoT nodes, robotics, or embedded systems, document the hardware architecture here. If your solution is 100% software/AI, you may indicate "Software-Only Solution" in this file.*

## 1. Hardware Overview
- **Prototype Status:** (e.g. Breadboard prototype / Custom PCB / Simulation in Wokwi)
- **Primary Microcontroller / SBC:** (e.g. ESP32 DevKit V1 / Raspberry Pi 4 / Arduino Uno)
- **Communication Protocol:** (e.g. WiFi MQTT / LoRaWAN 868MHz / BLE / GSM SMS)

---

## 2. Bill of Materials (BOM)
Detailed BOM is available in [`hardware/bom.csv`](file:///Users/laku/projects/agripreneurs-buildathon-template/hardware/bom.csv).

| Component | Quantity | Key Specifications | Estimated Cost (INR) |
|-----------|----------|--------------------|----------------------|
| Microcontroller | 1 | ESP32 (WiFi + BLE) | ₹450 |
| Soil Moisture Sensor | 2 | Capacitive v1.2 | ₹160 |
| Solenoid Valve | 1 | 12V DC 1/2" | ₹320 |
| Relay Module | 1 | 5V 1-Channel optocoupled | ₹65 |
| Solar Power Unit | 1 | 10W panel + 18650 battery | ₹600 |
| **Total Estimated Hardware Cost** | | | **₹1,595** |

---

## 3. Pinout & Interfacing Table

| Device / Module | Pin on Module | ESP32 / Arduino Pin | Signal Type (Digital / Analog / I2C / SPI) | Notes |
|-----------------|---------------|---------------------|---------------------------------------------|-------|
| Soil Moisture #1| AOUT          | GPIO 34 (ADC1_CH6)  | Analog Input (0-3.3V)                      | Calibrated dry=3200, wet=1400 |
| Relay Module    | IN            | GPIO 23             | Digital Output (HIGH = Active)             | Drives 12V solenoid |
| Status LED      | Anode         | GPIO 2              | Digital Output                             | Heartbeat indicator |

---

## 4. Power & Field Durability
- **Power Source:** (e.g. Solar panel with 18650 Li-ion battery backup or 12V DC adapter)
- **Operating Current:** (e.g. Active transmission: 180mA; Deep sleep: 15µA)
- **Battery Life Estimate:** (e.g. ~14 days without sunlight on 2500mAh cell with 15-minute sleep intervals)
- **Enclosure & Weatherproofing:** (e.g. IP65 junction box with cable glands)

---

## 5. Firmware Instructions
Firmware code is located in [`hardware/firmware/main.ino`](file:///Users/laku/projects/agripreneurs-buildathon-template/hardware/firmware/main.ino).
1. Open the sketch in Arduino IDE or VS Code with PlatformIO.
2. Select target board: `ESP32 Dev Module`.
3. Set upload speed to `115200`.
4. Flash firmware and open Serial Monitor at `115200 baud`.
