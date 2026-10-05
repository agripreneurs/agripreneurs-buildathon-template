# Selected Problem Statement

> **Buildathon Tracks:** Select one of the 6 official problem statements (PS1 - PS6) detailed in the keynote presentation, or choose the Open Innovation track for your team's original idea.

---

## 1. Track & Problem Statement Selection

- **Selected Track:** `[PS1 | PS2 | PS3 | PS4 | PS5 | PS6 | Open Innovation / Own Idea]`
- **Problem Statement Title:** `[Title of the problem statement or your own topic]`
- **Official Problem Tracks Reference:**
  - **PS1: Daily Price Signal** (Telugu WhatsApp price bot pulling Agmarknet daily open data via data.gov.in; single clear modal price, 7-day trend, nearest 3 markets).
  - **PS2: Storage Booking (Book, Hold, Sell Later)** (WDRA registered warehouse booking, digital e-receipt, 1-tap pledge loans, and selling after the post-harvest glut; e.g. dry chilli in AP).
  - **PS3: Grade-Assist (Three Grades, Four Checks, One Card)** (Objective farm-gate quality grading for tomatoes/produce; 4-question checklist + 3 proof photos -> QR grade card).
  - **PS4: Crop-Photo Check (Likely Issues, Honest Advice)** (Multi-photo WhatsApp diagnosis; top-3 likely causes with confidence, unbranded low-cost first steps, agronomist in the loop).
  - **PS5: Organic Marketplace on ONDC & Digi Rythu Bazaar** (Connecting certified organic growers to urban consumers; NPOP/PGS QR traceability, Rythu Bazaar seller nodes, fair pricing).
  - **PS6: Universal Robotic Farming Stack (KisaanBot / Urban Automated Farming)**:
    - *Challenge 1 (ECE/Mech):* Universal Tool-Head & Smart Pogo Bus (Kinematic auto-docking, EEPROM 1-Wire discovery, leak-free dosing).
    - *Challenge 2 (CS/AI):* FieldVision Homography & Scanner (ArUco calibration, lightweight YOLO, G-code generation).
    - *Challenge 3 (CS/Systems):* Universal Agronomic DSS & Bridge (Weather gating, TSP path solver, GRBL & Nav2 bridge).
  - **Open Innovation:** Mud storage, weed mat, hyperspectral seed analysis, cold-chain tracker, or your team's original farmer-validated problem.

---

## 2. Agricultural Ground Reality & Problem Context
*Describe the on-ground issue from the perspective of Andhra Pradesh / Indian smallholder farmers:*
- What specific pain point or value leak does this cause? (e.g. 30-40% post-harvest rot, distress sale at glut price, chemical dealer over-prescription)
- What is the current manual or traditional work-around? Why does it fail?
- What are the real field constraints? (e.g. Telugu vernacular, low smartphone literacy, intermittent network, dust/heat)

---

## 3. Reusable Modules & Rails Leveraged
*AgriPreneurs rule: **"Build the thin layer, not the whole stack."** Stand on existing rails and reusable modules.*

- **Existing Rails Leveraged:** (Check all that apply)
  - [ ] **Agmarknet / data.gov.in** (Open mandi pricing feed)
  - [ ] **ONDC** (Open Network for Digital Commerce)
  - [ ] **Digi Rythu Bazaar** (Farm-to-home delivery hubs in Visakhapatnam)
  - [ ] **WhatsApp Business / Twilio** (Telugu conversational channel)
  - [ ] **e-NAM / WDRA** (National market & warehouse receipt system)
- **Shared AgriPreneurs Modules Used:**
  - [ ] **M1:** Farmer Registry (`farmer.registered`, who, what they grow, where)
  - [ ] **M2:** Vernacular Messaging (WhatsApp hook, Telugu text/voice)
  - [ ] **M3:** Image and Inference (Leaf photos, camera calibration)
  - [ ] **M4:** Price Feed (Daily mandi price pattern & history)
  - [ ] **M5:** Advisory Engine (Honest, unbranded agronomic advice)
  - [ ] **M6:** Listing (Produce listed with provenance)
  - [ ] **M8:** Receipt & Ledger (e-receipt, UPI settlement)
  - [ ] **M9:** Traceability (QR code provenance tagging)

---

## 4. Target Beneficiaries & Persona
- **Primary Users:** (e.g., Smallholder dry chilli farmers in Gurazala/Guntur, Tomato growers in Vizag belt, FPO managers, Urban terrace gardeners)
- **Farmer Environment:** (e.g., Offline/2G conditions, keypad phone or basic Android, vernacular Telugu voice/text)

---

## 5. "One Honest Number" — Measured Field Metric
*The Buildathon requirement is to put your prototype in a real farmer's hands and report one honest number:*
- **Number of real farmers committed/tested:** (Target: minimum 5 farmers by 16 October)
- **One Honest Metric:** (e.g., "Farmer gained ₹300/quintal above local trader quote", "Grade card cut dispute time from 20 mins to 2 mins", "Avoided ₹1,200 needless pesticide spray")
- **Farmer Testimonial / Feedback:** What did the farmer actually say when holding the prototype?