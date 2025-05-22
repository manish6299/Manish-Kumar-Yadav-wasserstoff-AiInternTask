import sqlite3

def init_db():
    conn = sqlite3.connect("financials.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS metric_table (
            quarter TEXT,
            metric TEXT,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_metrics(data):
    conn = sqlite3.connect("financials.db")
    c = conn.cursor()
    c.executemany("INSERT INTO metric_table VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()
