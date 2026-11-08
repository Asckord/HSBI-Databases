import sqlite3
import time
from pathlib import Path
from uuid import uuid4

# База данных лежит рядом с этим скриптом
DB = Path(__file__).with_name("edge.db")
N = 10000


def benchmark(trigger_enabled):
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")

    # Включаем или выключаем тестовый триггер
    if trigger_enabled:
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS trg_benchmark
            AFTER INSERT ON reading
            FOR EACH ROW
            BEGIN
                INSERT INTO audit (
                    reading_id,
                    old_value,
                    new_value
                )
                VALUES (
                    NEW.reading_id,
                    NULL,
                    NEW.value
                );
            END;
        """)
    else:
        conn.execute("DROP TRIGGER IF EXISTS trg_benchmark")

    # Уникальные метки для каждого запуска
    run_id = uuid4().hex

    rows = [
        (2, f"benchmark-{run_id}-{i}", 1.5, 1)
        for i in range(N)
    ]

    # Измеряем время вставки
    start = time.perf_counter()

    conn.executemany("""
        INSERT INTO reading (
            sensor_id,
            ts,
            value,
            interval_s
        )
        VALUES (?, ?, ?, ?)
    """, rows)

    conn.commit()

    elapsed = time.perf_counter() - start

    # Удаляем тестовые записи и связанные записи аудита
    prefix = f"benchmark-{run_id}-%"

    conn.execute("""
        DELETE FROM audit
        WHERE reading_id IN (
            SELECT reading_id
            FROM reading
            WHERE ts LIKE ?
        )
    """, (prefix,))

    conn.execute(
        "DELETE FROM reading WHERE ts LIKE ?",
        (prefix,)
    )

    conn.commit()
    conn.close()

    return elapsed


# Два замера
without_trigger = benchmark(False)
with_trigger = benchmark(True)

# Вывод результатов
print(f"Без триггера: {without_trigger:.4f} сек.")
print(f"С триггером:  {with_trigger:.4f} сек.")
print(f"Разница:      {with_trigger - without_trigger:.4f} сек.")

if without_trigger > 0:
    overhead = (
        (with_trigger - without_trigger)
        / without_trigger
        * 100
    )
    print(f"Накладные расходы: {overhead:.2f}%")