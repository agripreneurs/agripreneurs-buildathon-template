# Data Directory

This directory contains sample and lightweight reference data for your prototype.

## Important Guidelines: Git & Large Datasets
1. **Never commit large datasets (>10 MB) to Git.**
   - Git repositories become sluggish and exceed GitHub push limits.
   - Large raw datasets (e.g. satellite GeoTIFFs, high-res drone images, video feeds, multi-gigabyte CSVs) must be hosted on cloud storage:
     - Google Drive / OneDrive / Dropbox (ensure access is set to "Anyone with the link can view")
     - Kaggle Datasets
     - Hugging Face Datasets
     - AWS S3 / Google Cloud Storage
2. **Provide Download Scripts or Instructions:**
   - If your model or application requires external data, provide an automated download script in `src/` (e.g. `python src/download_data.py`) or document exact download links in this file.
3. **Keep `data/sample_data.csv` Light:**
   - The sample file in this folder is intended for offline unit testing, CI pipelines, and demonstration purposes.

---

## Dataset Description (For Your Solution)
*Fill this section with details about the data your solution relies on:*

- **Data Source(s):** (e.g. On-field IoT Sensors, Government Open Data / Agmarknet, Sentinel-2 Satellite imagery, PlantVillage dataset, Kaggle)
- **Data Format:** (e.g. CSV, JSON, GeoJSON, Images)
- **Data Size:** (e.g. 5 MB sample, 2 GB full dataset)
- **External Dataset Link:** `[Link to dataset if hosted externally]`
- **Data Schema:**

| Column / Field Name | Data Type | Unit / Range | Description |
|---------------------|-----------|--------------|-------------|
| `timestamp`         | ISO 8601  | YYYY-MM-DD HH:MM:SS | Time of sensor observation |
| `soil_moisture_pct` | Float     | 0 - 100 %    | Volumetric soil water content |
| `soil_temp_c`       | Float     | Celsius      | Soil probe temperature |
| `ambient_temp_c`    | Float     | Celsius      | Ambient air temperature |
| `humidity_pct`      | Float     | 0 - 100 %    | Relative air humidity |
| `npk_nitrogen_mgkg` | Float     | mg/kg        | Soil nitrogen reading |
| `npk_phosphorus_mgkg`| Float    | mg/kg        | Soil phosphorus reading |
| `npk_potassium_mgkg`| Float     | mg/kg        | Soil potassium reading |
| `irrigation_status` | Integer   | 0 = Off, 1 = On | Current valve state |
