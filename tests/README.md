# Testing Directory (`/tests`)

This directory houses automated tests and validation scripts for your solution.

## Running Tests

### Standard Python Unittest (Zero setup required)
```bash
python3 -m unittest discover tests
```

### Pytest (If installed)
```bash
pytest tests/ -v
```

### JavaScript / Node.js (If using npm)
```bash
npm test
```

---

## What Judges Look for in Testing & Validation
Judges award significant points to engineering maturity and reliability:
1. **Unit Tests:** Verify that critical functions (e.g., formula calculations, sensor thresholds, input sanitization) behave as expected.
2. **Edge Cases:** Test boundary conditions (e.g., missing sensor data, disconnected IoT nodes, out-of-range sensor readings like negative soil moisture).
3. **Integration & Hardware Simulation:** If physical hardware is unavailable during grading, provide mock scripts or simulated test feeds so judges can run and verify your system without needing a physical sensor connected.
