import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("edge.db")

rows = [
    (1, "2026-03-01 08:00:00", 41.7, 1),
    (2, "2026-03-01 08:00:01", 2.1, 1)
]

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    conn.executemany("""
        INSERT INTO reading(sensor_id, ts, value, interval_s)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(sensor_id, ts)
        DO UPDATE SET value = excluded.value
    """, rows)

    count = conn.execute(
        "SELECT COUNT(*) FROM reading"
    ).fetchone()[0]

    print("Total readings:", count)
