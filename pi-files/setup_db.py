import os
import psycopg2
from dotenv import load_dotenv

# 1. Load config from .env
load_dotenv()

def get_db_connection():
    """Connects to Postgres using .env credentials"""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST', '127.0.0.1'),
            port=os.getenv('DB_PORT', '5432')
        )
        return conn
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

def prepare_tables(conn):
    """Creates separate tables if they don't exist"""
    if not conn:
        return

    with conn.cursor() as cur:
        # Create Weather Table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id SERIAL PRIMARY KEY,
                captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                payload JSONB
            );
        """)
        # Create Spotify Table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS spotify_data (
                id SERIAL PRIMARY KEY,
                captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                payload JSONB
            );
        """)
    conn.commit()
    print("✅ Database Platform Ready: 'weather_data' and 'spotify_data' tables verified.")

# --- EXECUTION FLOW ---
if __name__ == "__main__":
    db_conn = get_db_connection()

    if db_conn:
        prepare_tables(db_conn)
        db_conn.close()
        print("🏁 Infrastructure setup complete.")
