# 🌾 Agripreneurs Buildathon 01 - Submission Guidelines

Welcome to the **Agripreneurs Buildathon 01**! This document outlines everything you need to know about preparing your solution, organizing your repository, and submitting your project on time.

---

## 📅 Key Deadlines & Timeline

| Event | Date & Time | Notes |
|-------|-------------|-------|
| **Submission Deadline** | **15 October 2026, 11:59 PM IST** | Strict deadline. Late commits will not be evaluated. |
| **Shortlist Announcement** | To be notified | Finalist teams announced for live presentation. |
| **Live Pitch & Q&A** | To be scheduled | Live virtual presentation before the judging panel. |

> **Timezone Specificity:** All times are in **Indian Standard Time (IST, UTC +5:30)**. Please adjust for your local timezone accordingly.

---

## 👥 Team Composition & Speaker Rules

- **Team Size:** Recommended **2 to 5 members** per team.
- **Live Q&A Speakers:** **Maximum 3 speakers** per team during the live pitch and judge Q&A session. Other members may attend to assist with technical demonstrations or audio/video support.
- **Multidisciplinary Teams:** We strongly recommend teams combine software, electronics/hardware, agricultural domain knowledge, and product design.

---

## 🎯 Problem Statement Tracks

Teams can choose either one of the 6 official problem statements or propose their own idea:

1. **Track PS1:** Precision Irrigation & Water Resource Optimization (IoT / Soil Sensors / Drip Actuation)
2. **Track PS2:** Crop Pest & Disease Early Detection (Computer Vision / Drone / Mobile Edge AI)
3. **Track PS3:** Soil Health & Nutrient Management (NPK sensing / Fertilizer Advisory / Soil Testing)
4. **Track PS4:** Post-Harvest Loss Prevention & Cold Chain Monitoring (Smart Storage / Spoilage Detection)
5. **Track PS5:** Farm Mechanization & Affordable Automation (Smallholder robotics / Seeders / Weeding tools)
6. **Track PS6:** Market Linkage, Price Discovery & Fair Supply Chains (Fintech / Direct Farmer-to-Consumer / Mandi API)
7. **Track 07 (Open Innovation):** Original student-identified agricultural problem statement

---

## 🛠️ Repository Organization & Skeleton Structure

Your submission must follow this standard folder layout:

```text
├── .env.example              <- Template for environment variables (DO NOT commit secrets!)
├── .gitignore                <- Blocks secrets, build caches, and ML weights
├── README.md                 <- PRIMARY source of truth for your project
├── SUBMISSION_GUIDELINES.md  <- This guide
├── requirements.txt          <- Python dependencies (or package.json if JS/Node)
├── docs/                     <- Documentation & deliverables
│   ├── problem-statement.md  <- Details on your selected problem statement
│   ├── solution-overview.md  <- How your solution works
│   ├── system-architecture.md<- Mermaid diagrams & data flow
│   ├── executive-summary-template.md <- 1-page executive summary template
│   ├── presentation-guidelines.md    <- Pitch deck tips & structure
│   ├── final-report-template.md      <- (Optional) deep-dive technical paper
│   ├── presentation.pdf      <- Your pitch deck (or provide cloud link in README)
│   └── project-report.pdf    <- (Optional) deep-dive or 1-page executive summary PDF
├── src/                      <- Application & algorithmic source code
│   ├── __init__.py
│   ├── main.py               <- Prototype entrypoint
│   └── utils.py              <- Data processing and utility helpers
├── tests/                    <- Automated tests & validation scripts
│   ├── __init__.py
│   └── test_basic.py         <- Unit tests
├── hardware/                 <- Hardware, IoT, circuits, and firmware
│   ├── README.md             <- Hardware pinout, sensors, and power design
│   ├── bom.csv               <- Bill of Materials (components, cost, links)
│   ├── firmware/             <- Arduino / ESP32 / C++ / MicroPython sketches
│   └── schematics/           <- Circuit diagrams, wiring images, CAD/STL files
└── data/                     <- Sample datasets and schemas
    ├── README.md             <- Dataset documentation and external links
    └── sample_data.csv       <- Lightweight sample dataset for testing
```

---

## ⚡ Engineering Focus vs. Deliverable Burden

> **Important Philosophy:** We value working prototypes, solid engineering, and real-world farm usability over paper documentation. 
> 
> - **Do NOT spend days writing a 40-page report.**
> - All essential documentation should be consolidated into your `README.md` and repository markdown files.
> - A **concise 1-page executive summary** ([`docs/executive-summary-template.md`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/executive-summary-template.md)) alongside your pitch deck ([`docs/presentation.pdf`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/presentation.pdf) or cloud link) completely replaces long reports.
> - The comprehensive report template ([`docs/final-report-template.md`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/final-report-template.md)) is **strictly optional** and reserved only for teams wanting to submit research-grade papers.

---

## 🔒 GitHub Submission & Repository Access

Teams may build in a private or public repository:

### If your repository is PRIVATE:
To allow organizers and judges to review your code, commit history, and tests before and during judging, you **MUST add the official judge GitHub accounts as collaborators**:
1. Go to your repository on GitHub: `Settings` $\rightarrow$ `Collaborators` $\rightarrow$ `Add people`.
2. Add both judge/organizer accounts:
   - **[`@agripreneurs`](https://github.com/agripreneurs)**
   - **[`@kumarraja`](https://github.com/kumarraja)**
3. Ensure the invitation has been sent before the deadline.

### If your repository is PUBLIC:
Ensure the repository visibility is public and the URL is accessible to anyone.

---

## 📦 Required Deliverables

Every team must deliver:

1. **GitHub Repository:** Clean code, modular structure, working tests, and populated `README.md`.
2. **Pitch Deck (Presentation):**
   - 8–10 slides following [`docs/presentation-guidelines.md`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/presentation-guidelines.md).
   - Saved as [`/docs/presentation.pdf`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/presentation.pdf) **OR** shared via a public cloud link (Google Slides / Canva / Notion with "Anyone with link can view").
3. **Working Prototype Video Demo:**
   - 2 to 3 minutes duration.
   - Uploaded to **YouTube (Unlisted or Public)** or Loom.
   - Demonstrates the software running, hardware operating (if applicable), and real sensor/model outputs.
4. **1-Page Executive Summary:**
   - Filled out in [`docs/executive-summary-template.md`](file:///Users/laku/projects/agripreneurs-buildathon-template/docs/executive-summary-template.md) or committed as `/docs/project-report.pdf` (or cloud link).
5. **Live Deployed Prototype URL (Optional but recommended):**
   - E.g. Vercel, Render, Streamlit Cloud, Hugging Face Spaces, or mobile APK download.

---

## 📝 Submission Form Format (Purely Text & URL Based)

To ensure zero upload failures or file size errors, the official submission form is **purely text- and URL-based**. You will submit:

1. Team Name
2. Selected Track (PS1 - PS6 or Open Innovation)
3. GitHub Repository URL (e.g. `https://github.com/team-name/agripreneurs-solution`)
4. Video Demo URL (e.g. YouTube Unlisted link: `https://youtu.be/...`)
5. Presentation Deck URL (or specify `In repo: /docs/presentation.pdf`)
6. Executive Summary URL (or specify `In repo: /docs/executive-summary-template.md`)
7. Live Deployed Web/API URL (Optional)
8. Team Members' Names, Emails, Institutions
9. Designated Live Q&A Speakers (Max 3 names)

---

## 🏆 Evaluation Criteria

Judges will score solutions based on five key dimensions:

| Criterion | Weight | What Judges Look For |
|-----------|--------|----------------------|
| **1. Ground Reality & Agricultural Impact** | **25%** | Does the solution address genuine farmer pain points? Is it affordable and feasible in rural Indian field conditions? |
| **2. Technical Execution & Engineering Rigor** | **25%** | Quality of code, circuit design/BOM, working unit tests, clean architecture, and error resilience. |
| **3. Innovation & Originality** | **20%** | Novel approach, creative use of sensors/AI/mechanics, and clear differentiation from existing market tools. |
| **4. Unit Economics & Scalability** | **15%** | Low manufacturing/maintenance cost, viable business or FPO model, rapid payback period for smallholder farmers. |
| **5. Prototype Demo & Live Q&A** | **15%** | Clarity of pitch, working proof demonstrated in the video/live prototype, and domain mastery during judge Q&A (max 3 speakers). |

---

## ✅ Final Pre-Submission Checklist

Before submitting on **15 October 2026, 11:59 PM IST**, verify:

- [ ] Repository has no hardcoded secrets, tokens, or API keys (`.env.example` used instead).
- [ ] Large ML models and raw data archives are not committed to git (stored on cloud storage).
- [ ] `README.md` is fully filled out with team names, problem statement, architecture, setup steps, and demo links.
- [ ] If private, collaborators `@agripreneurs` and `@kumarraja` have been added.
- [ ] Video demo (2-3 min) is uploaded and test-viewed in an incognito window.
- [ ] Slide deck (`docs/presentation.pdf` or cloud link) is accessible without login barriers.
- [ ] Code runs successfully from instructions in `README.md` (`python src/main.py` and `python -m unittest discover tests`).
- [ ] Hardware BOM (`hardware/bom.csv`) and circuit schematics are documented (if applicable).
- [ ] 3 designated speakers are identified for the live pitch.
- [ ] Submission form is submitted before **11:59 PM IST, 15 October 2026**.
