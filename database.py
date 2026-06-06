import sqlite3
from pathlib import Path

DB_PATH = "db/asset_requests.db"


def init_db():
    Path("db").mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asset_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id TEXT UNIQUE,
            employee_id TEXT,
            asset_type TEXT,
            asset_name TEXT,
            justification TEXT,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_request(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO asset_requests (
            request_id,
            employee_id,
            asset_type,
            asset_name,
            justification,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["request_id"],
        data["employee_id"],
        data["asset_type"],
        data["asset_name"],
        data["justification"],
        data["status"]
    ))

    conn.commit()
    conn.close()


def get_all_requests():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM asset_requests")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_status(request_id, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE asset_requests SET status=? WHERE request_id=?",
        (status, request_id)
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")