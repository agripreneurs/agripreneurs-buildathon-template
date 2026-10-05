# Source Code Directory (`/src`)

This directory is the home for your application logic, algorithms, models, and services.

## Suggested Structure (Choose what fits your solution)

Depending on your solution type, here are recommended organizational patterns:

### Option A: Python Backend / Machine Learning / Data Processing
```text
src/
├── __init__.py
├── main.py              # Application entrypoint
├── utils.py             # Shared utilities & data loaders
├── api/                 # FastAPI / Flask REST API endpoints
├── models/              # Inference scripts, feature extraction, ML pipelines
└── services/            # IoT ingest, notifications, database connectors
```

### Option B: Full-Stack Web Application (e.g. Next.js / React / Vue)
```text
src/
├── components/          # Reusable UI widgets (cards, charts, maps)
├── pages/ or app/       # Route pages (Dashboard, Analytics, Alerts)
├── lib/ or services/    # API clients, auth helpers, socket listeners
└── styles/              # Global CSS / theme tokens
```

### Option C: Mobile Application (Flutter / React Native)
```text
src/
├── screens/             # Farmer-facing mobile screens
├── widgets/             # Custom UI widgets
├── providers/ / bloc/   # State management
└── services/            # Bluetooth BLE, HTTP API, offline storage
```

---

## Coding Standards & Engineering Best Practices
1. **Modular Code:** Break code into reusable functions and classes rather than one 2,000-line script.
2. **Configuration via Environment:** Use `.env` (via `python-dotenv` or equivalent) for ports, URLs, and secrets. **Never hardcode passwords or API keys.**
3. **Clear Comments & Docstrings:** Write brief docstrings explaining input arguments and return values.
4. **Error Handling:** Gracefully handle network timeouts, missing sensor values, and offline conditions (very common in agricultural field conditions).
