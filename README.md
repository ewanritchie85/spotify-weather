# Spotify & Weather Data Platform

A dedicated data warehouse hosted on a Raspberry Pi (Ubuntu 24.04) designed to collect, store, and analyze Spotify listening habits alongside local weather data.

---

## 🏗️ Infrastructure Summary

This platform is configured as a **Headless Database Server**. The Raspberry Pi acts as the central storage hub, while data processing and visualization are intended to be handled by a remote Jupyter Notebook.

### 1. Database Configuration (PostgreSQL 16)
The system uses PostgreSQL with a custom schema optimized for JSONB storage, allowing for flexible API payload archiving.

| Component | Setting |
| :--- | :--- |
| **Database Name** | `spotify_weather` |
| **Primary User** | `<your Postgres user>` |
| **Port** | `5432` |
| **Auth Method** | `md5` (Password-based) |

### 2. Networking & Remote Access
To allow the Jupyter Notebook on your main computer to communicate with the Pi, the following changes were applied:
* **Listener**: `postgresql.conf` updated to `listen_addresses = '*'`
* **Security**: `pg_hba.conf` updated to allow `0.0.0.0/0` (Local Network)
* **Permissions**: Explicitly granted `ALL` permissions on the `public` schema to the project user.

---

## 📂 Project Structure

```text
~/spotify-weather-project/
├── venv/               # Isolated Python environment
├── .env                # API Keys & Database credentials
├── init_db.py          # Infrastructure "Table-Setter" script
└── .cache              # Spotify OAuth token (Auto-generated)

```

### Management Tools (pi-files)

The platform is managed via a combination of Bash automation and Python initialization scripts.

**Global Command:** `setup-spotify-weather`

- Located at `/usr/local/bin/`, this script automates the entire environment lifecycle:
    - **System Check:** Installs `libpq-dev`, `python3-venv`, and `postgresql-client`.
    - **Environment Sync:** Rebuilds/checks the Python Virtual Environment.
    - **Dependency Management:** Installs `psycopg2-binary` and `python-dotenv`.
    - **Auto-Init:** Executes `setup_db.py` to verify or create the database tables.

### Logic Script: `setup_db.py`

A Python script that acts as the "Architect." It ensures the PostgreSQL warehouse has the following structure:

- **weather_data**: Table for Met Office 3-hourly forecast JSON payloads.
- **spotify_data**: Table for Spotify "Recently Played" track history JSON payloads.

Both tables include:
- `id` (Primary Key)
- `captured_at` (Timestamp)
- `payload` (JSONB)

---

## 📡 Future Connection (Jupyter)

To pull data from this Pi onto your main computer, use the following connection logic in your Notebook:

```python
import psycopg2

# Connect to the Pi's IP address
conn = psycopg2.connect(
        host="<YOUR_PI_IP_ADDRESS>",
        database="spotify_weather",
        user="ewanritchie",
        password="your_password"
)
```
