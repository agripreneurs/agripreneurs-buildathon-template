"""Utility functions for agricultural data processing and environment configuration."""

import csv
import os
from typing import Dict, List, Optional
from pathlib import Path


def get_project_root() -> Path:
    """Return the absolute path to the project root directory."""
    return Path(__file__).resolve().parent.parent


def load_sensor_data(filepath: Optional[Path] = None) -> List[Dict[str, str]]:
    """
    Load sensor observations from CSV file.
    Defaults to data/sample_data.csv if filepath is not provided.
    """
    if filepath is None:
        filepath = get_project_root() / "data" / "sample_data.csv"

    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found at: {filepath}")

    records = []
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records


def evaluate_irrigation_need(
    soil_moisture_pct: float,
    threshold_pct: float = 25.0
) -> Dict[str, any]:
    """
    Evaluate whether irrigation should be triggered based on soil moisture.
    
    Args:
        soil_moisture_pct: Current soil moisture percentage (0-100%).
        threshold_pct: Threshold below which irrigation is recommended.
        
    Returns:
        Dict containing irrigation recommendation, urgency, and current reading.
    """
    if soil_moisture_pct < 0 or soil_moisture_pct > 100:
        raise ValueError("Soil moisture must be between 0 and 100%.")

    trigger_irrigation = soil_moisture_pct < threshold_pct
    urgency = "HIGH" if soil_moisture_pct <= (threshold_pct - 10) else ("MEDIUM" if trigger_irrigation else "LOW")

    return {
        "soil_moisture_pct": soil_moisture_pct,
        "threshold_pct": threshold_pct,
        "trigger_irrigation": trigger_irrigation,
        "urgency": urgency,
        "recommendation": "Activate drip irrigation valve" if trigger_irrigation else "Moisture level adequate"
    }
