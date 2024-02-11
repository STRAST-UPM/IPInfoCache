import fastapi
import sqlite3
from datetime import datetime, timedelta

app = fastapi.FastAPI()


def get_db():
    db = sqlite3.connect("/db/db.sqlite3")
    return db


db = sqlite3.connect("/db/db.sqlite3")

db.execute(
    "CREATE TABLE IF NOT EXISTS cache (ip TEXT PRIMARY KEY, value TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


class CacheItem:
    def __init__(self, ip, value, created_at=None):
        self.ip = ip
        self.value = value
        self.created_at = created_at


# create a mapper between the Cache class and the cache table
def map_row_to_cache(row):
    return CacheItem(row[0], row[1],
                     datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"))


@app.get("/ip/{ip}")
def get_ip(ip: str):
    cursor = get_db().execute("SELECT * FROM cache WHERE ip = ?", (ip,))
    row = cursor.fetchone()
    if row:
        item = map_row_to_cache(row)
        if item.created_at < datetime.now() - timedelta(days=30):
            return get_val(ip)
        else:
            return {"ip": ip, "value": item.value}
    else:
        return get_val(ip)


@app.get("/ip_all")
def get_all_ip():
    cursor = get_db().execute("SELECT * FROM cache")
    rows = cursor.fetchall()
    return [map_row_to_cache(row) for row in rows]


def get_val(ip):
    value = "unknown"
    db = get_db()
    db.execute("INSERT INTO cache (ip, value) VALUES (?, ?)", (ip, value))
    db.commit()
    db.close()

    return {"ip": ip, "value": value}