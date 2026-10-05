"""
Main entry point for the Agripreneurs Buildathon project prototype.
Replace or extend this script with your application logic (CLI, API server, or pipeline).
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.utils import load_sensor_data, evaluate_irrigation_need


def main():
    print("=" * 60)
    print("🌾 Agripreneurs Buildathon 01 - Solution Prototype Entrypoint")
    print("=" * 60)

    try:
        data = load_sensor_data()
        print(f" Loaded {len(data)} sample sensor observations from data/sample_data.csv\n")

        print("🔍 Evaluating Soil Moisture & Irrigation Recommendations:")
        print("-" * 60)
        for i, row in enumerate(data, start=1):
            ts = row.get("timestamp", "N/A")
            moisture = float(row.get("soil_moisture_pct", 0.0))
            result = evaluate_irrigation_need(moisture, threshold_pct=25.0)

            status_icon = "🚨" if result["trigger_irrigation"] else "✅"
            print(f"[{i}] {ts} | Moisture: {moisture:>5.1f}% | Action: {result['recommendation']} [{result['urgency']}] {status_icon}")

        print("\n" + "=" * 60)
        print("💡 Next Steps for Your Team:")
        print(" 1. Replace this starter script with your actual model/service/dashboard.")
        print(" 2. Place hardware code in /hardware/firmware.")
        print(" 3. Document your architecture in README.md.")
        print("=" * 60)

    except Exception as e:
        print(f"❌ Error during prototype execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
