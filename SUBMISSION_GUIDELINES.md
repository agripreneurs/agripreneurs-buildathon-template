# 🌾 Agripreneurs Buildathon 01 - Submission & Engineering Guidelines

> **Theme:** *Build for the Farmer. Start in the field, not on the whiteboard.*  
> **Initiative by:** AgriPreneurs · Partners: AI for Vizag, AI Karyashala, Quantamizers, GDG Vizag · Support: RTIH, G-TEC, VDC  
> **Venues:** Kickoff at RTIH (Siripuram) | Live Showcase Meet at **GITAM VDC, Vizag** & Real Farming Communities

---

## 📅 Official Buildathon Timeline

| Milestone | Date & Time (IST) | Description |
|-----------|-------------------|-------------|
| **Kickoff & Tribe Formation** | Sunday, 4 Oct 2026 | Keynote, problem pitches, tribe matching at RTIH Vizag |
| **Field Sprints & Coding** | 4 Oct – 15 Oct 2026 | Building the smallest real version; testing with local farmers |
| **GitHub Submission Deadline** | **Thursday, 15 Oct 2026, 11:59 PM IST** | **Strict code freeze.** Commits after this time will not be evaluated |
| **Field Commit Benchmark** | Friday, 16 Oct 2026 | Commit prototype to 5 real farmers; record the "one honest number" |
| **AgriPreneurs Showcase Meet** | **Saturday, 17 Oct 2026** | **Live showcase floor at GITAM VDC, Vizag.** Working demo & farmer feedback |
| **Soil-Grown Ventures Graduation**| December 2026 | Top builds showcase at **AgriPreneurs Day @ Visakha Organic Mela** |

---

## 👥 Tribe Composition & Speaker Rules

- **Team Size:** Recommended **2 to 5 members** per Tribe.
- **Multidisciplinary Tribes:** Mix developers (Python, React, Node), designers (plain Telugu flows), IoT/hardware builders (sensors, boards), product managers, and farm domain voices.
- **Live Showcase Speakers:** **Maximum 3 speakers** per team during the live pitch and judge Q&A session. Other team members may assist with physical hardware or live screen demonstrations.

---

## 🎯 The 6 Official Problem Statements

Teams select one of the 6 official problem statements or choose the Open Innovation track:

1. **PS1: Daily Price Signal**  
   *The Challenge:* Open mandi prices sit in complex English tables (~16k rows/day, 3 prices per variety). Farmers sell blind to middlemen.  
   *The Build:* A Telugu WhatsApp reply with today's mandi price, modal per quintal and per kg, 7-day trend, and nearest 3 markets from Agmarknet open data (`data.gov.in`).  
   *Modules:* M1 Registry · M2 Messaging · M4 Price Feed.

2. **PS2: Storage Booking (Book, Hold, Sell Later)**  
   *The Challenge:* Farmers sell at harvest glut because loans fall due and they don't know which WDRA registered warehouses have space.  
   *The Build:* Reserve a storage slot before harvest with a small UPI advance; receive a verifiable digital receipt; 1-tap pledge loan; sell on e-NAM/ONDC when price rises.  
   *Modules:* M1 Registry · M4 Price Feed · M6 Listing · M8 Receipt & Ledger.

3. **PS3: Grade-Assist (Three Grades, Four Checks, One Card)**  
   *The Challenge:* Quality is unrewarded at the farm gate because assaying is subjective, slow, and lab-bound.  
   *The Build:* 4 visible checks (size, colour, damage, cleanliness) + 3 photos generate a verified Grade Card (image + QR) that buyers trust. Start with tomatoes.  
   *Modules:* M1 Registry · M2 Messaging · M3 Image & Inference · M8 Receipt & Ledger.

4. **PS4: Crop-Photo Check (Likely Issues, Honest Advice)**  
   *The Challenge:* Look-alike symptoms lead to chemical over-prescription by input dealers. AI apps give single overconfident answers with ads.  
   *The Build:* Farmer sends leaf photos on WhatsApp; receives top-3 likely issues with confidence, low-cost/unbranded first steps, and human agronomist review.  
   *Modules:* M1 Registry · M2 Messaging · M3 Image & Inference · M5 Advisory.

5. **PS5: Organic Marketplace on ONDC and Digi Rythu Bazaar**  
   *The Challenge:* Organic farmers sell at conventional prices because buyers cannot verify organic authenticity without visible proof.  
   *The Build:* Verified organic identity (NPOP/PGS QR trace); Rythu Bazaar hubs act as ONDC seller nodes; direct pricing raises farmer share from ₹22 to ₹42 on a ₹60 lot.  
   *Modules:* M1 Registry · M6 Listing · M8 Receipt & Ledger · M9 Traceability.

6. **PS6: Universal Robotic Farming Stack (Automated Farming / Farm Robotics)**  
   *The Challenge:* Cartesian farm robots require robust sub-systems for planting, scanning, and targeted dosing.  
   *The Build (Pick a Subsystem Challenge):*  
   - *Challenge 1 (ECE/Mech):* Universal Tool-Head & Smart Pogo Bus (kinematic auto-docking, EEPROM 1-Wire discovery, leak-free auto-valved dosing). Target: 20 auto-dock cycles & ≤±5% liquid variance.  
   - *Challenge 2 (CS/AI):* FieldVision Homography & Scanner (ArUco calibration, lightweight YOLO crop/weed detection, G-code stream). Target: ≤2.5 mm spatial accuracy & <2s inference.  
   - *Challenge 3 (CS/Systems):* Universal Agronomic DSS & Bridge (weather gating, TSP path solver, dual GRBL & Nav2 output). Target: 100% automated dispatch.

- **Open Innovation Track:** Low-cost storage, natural weed management, post-harvest quality testing, supply-chain monitoring, or your team's original farmer-validated problem.

---

## 🏛️ Architecture Philosophy: "Build the Thin Layer"

1. **Stand on Existing Rails (Do NOT Reinvent):**  
   Leverage Agmarknet / `data.gov.in`, ONDC, Digi Rythu Bazaar, WhatsApp Business, and e-NAM. Build the thin layer that connects the farmer to the rail.
2. **Reuse Shared Modules (M1–M10):**  
   Modules live under [`github.com/agripreneurs`](https://github.com/agripreneurs). Connect to them via published contracts and events only. **Never import another module's database directly.**
3. **Zero-Setup Default:**  
   Your code must run with **one command** and zero external paid cloud dependencies in its default form (using SQLite, mock data, or sample CSVs).
4. **Publish Contracts in `/spec`:**  
   Every module or service must publish its API or domain event contract in [`/spec`](file:///Users/laku/projects/agripreneurs-buildathon-template/spec/README.md).

---

## 🔒 GitHub Submission & Collaborator Setup

- **Submission Repository:** Push your code, docs, and deliverables to your team's GitHub repository.
- **Collaborator Rule for Private Repos:**  
  If your repository is kept private during the buildathon, you **MUST add the official judge and organizer GitHub accounts as collaborators** before the deadline:
  - **[`@agripreneurs`](https://github.com/agripreneurs)**
  - **[`@kumarraja`](https://github.com/kumarraja)**
- **Public Repositories:** Ensure repository visibility is public before **15 October 2026, 11:59 PM IST**.

---

## 📦 What to Submit (Purely Text- & URL-Based)

To avoid 50 MB upload limits and file corruption, the submission form is **purely text- and URL-based**:

1. **GitHub Repository URL:** Contains clean code, `/spec` contract, working tests, and documentation.
2. **Working Video Demo (2–3 Minutes):** Unlisted YouTube or Loom link demonstrating real software or hardware running.
3. **Pitch Deck (Slides):** 8–10 slides hosted at [`/docs/presentation.pdf`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/presentation.pdf) or a public Google Slides/Canva link.
4. **1-Page Executive Summary:** Filled out in [`docs/executive-summary-template.md`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/executive-summary-template.md) or committed as `/docs/project-report.pdf` (No 40-page reports required!).
5. **The One Honest Number:** State the metric achieved with real farmers (e.g. "Tested with 5 tomato farmers in Anandapuram; 100% agreed on Grade A card; saved ₹400/lot").
6. **Live Deployed URL (Optional):** Vercel, Streamlit Cloud, or APK link.
7. **Tribe Member Names & Max 3 Live Q&A Speakers.**

---

## 🏆 Judging Criteria

| Criterion | Weight | What Judges Look For |
|-----------|--------|----------------------|
| **1. Ground Truth & Farmer Impact** | **25%** | Does it solve a real value leak? Did you talk to farmers? Is it usable in plain Telugu / offline field conditions? |
| **2. Field Validation & "One Honest Number"** | **25%** | Did you test with 5 real farmers? What was the measured before/after metric? What did the farmer actually say? |
| **3. Technical Execution & Contract Rigor** | **20%** | Clean code, `/spec` contract, passing tests, zero-setup runnable default, and thin-layer reuse of existing rails. |
| **4. Frugal Engineering & Unit Economics** | **15%** | Low BOM cost (<₹1,500 for IoT), no unnecessary subscriptions, clear ROI for the farmer. |
| **5. Live Demo & Q&A Mastery** | **15%** | A working prototype (not just slides), clarity on what is *not* built yet, and domain grasp during Q&A (max 3 speakers). |

---

## ✅ Pre-Submission Checklist

Before **15 October 2026, 11:59 PM IST**:

- [ ] Zero secrets or API keys committed (`.env.example` provided).
- [ ] No large ML checkpoints or massive datasets committed to git.
- [ ] Starter script runs out of the box (`python3 src/main.py`).
- [ ] Automated tests pass (`python3 -m unittest discover tests`).
- [ ] Module contract or event schema defined in `/spec`.
- [ ] `README.md` fully completed with architecture diagram, tech stack, and links.
- [ ] 2–3 minute video demo recorded and viewable via unlisted YouTube/Loom.
- [ ] Pitch deck saved as `docs/presentation.pdf` or cloud URL set to public view.
- [ ] Tested with real farmers and "One Honest Number" documented.
- [ ] Collaborators `@agripreneurs` and `@kumarraja` added (if repo is private).
- [ ] Submission form completed before deadline.
