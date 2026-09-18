# telemetryac 🏎️📊

`telemetryac` is a Python-based telemetry logger for **Assetto Corsa**. It captures live vehicle data from the game and exports it into clean, structured CSV files, making it easy to analyze your driving performance, build custom dashboards, or train machine learning models.

## 🚀 Features

- **Live Telemetry Capture:** Logs high-frequency vehicle physics data (speed, RPM, gear, inputs, etc.) while you drive.
- **Lap Tracking:** Automatically detects lap completions and records session summaries.
- **Synchronized Data:** Automatically adjusts Assetto Corsa's raw 0-indexed lap states into intuitive, 1-indexed lap numbers so your telemetry aligns perfectly with your lap summaries.
- **Analysis-Ready Output:** Exports directly to standard CSV formats optimized for Pandas, SQL, or Excel.

---

## 📂 Data Output

The logger generates two primary CSV files that are designed to be easily joined together for analysis:

1. **`samples.csv`**  
   The high-frequency time-series data. Each row represents a single physics sample (e.g., throttle, brake, steering angle, speed) stamped with the current time and `lap` number.

2. **`laps.csv`**  
   The session summary data. Each row represents a single completed lap, containing aggregated metrics like lap times, sectors, and the `lap` identifier.

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DenoFury/telemetryac.git](https://github.com/DenoFury/telemetryac.git)
   cd telemetryac