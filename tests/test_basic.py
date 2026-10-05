"""
Basic test suite for project utilities and core logic.
Run with:
    python3 -m unittest discover tests
or:
    pytest tests/
"""

import unittest
from pathlib import Path
import sys

# Ensure src is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.utils import load_sensor_data, evaluate_irrigation_need, get_project_root


class TestAgriSolution(unittest.TestCase):

    def test_project_root_exists(self):
        """Verify project root path resolves correctly."""
        root = get_project_root()
        self.assertTrue(root.exists())
        self.assertTrue((root / "README.md").exists())

    def test_load_sample_sensor_data(self):
        """Verify that sample agricultural dataset loads and contains required fields."""
        data = load_sensor_data()
        self.assertGreater(len(data), 0, "Sample data should have at least 1 record")

        first_record = data[0]
        required_keys = ["timestamp", "soil_moisture_pct", "soil_temp_c", "humidity_pct"]
        for key in required_keys:
            self.assertIn(key, first_record, f"Missing expected key: {key}")

    def test_irrigation_evaluation_low_moisture(self):
        """Test irrigation trigger when moisture is below threshold."""
        result = evaluate_irrigation_need(soil_moisture_pct=15.0, threshold_pct=25.0)
        self.assertTrue(result["trigger_irrigation"])
        self.assertEqual(result["urgency"], "HIGH")

    def test_irrigation_evaluation_adequate_moisture(self):
        """Test irrigation trigger when moisture is sufficient."""
        result = evaluate_irrigation_need(soil_moisture_pct=35.0, threshold_pct=25.0)
        self.assertFalse(result["trigger_irrigation"])
        self.assertEqual(result["urgency"], "LOW")

    def test_irrigation_evaluation_invalid_input(self):
        """Test error handling on invalid percentage."""
        with self.assertRaises(ValueError):
            evaluate_irrigation_need(soil_moisture_pct=120.0)


if __name__ == "__main__":
    unittest.main()
