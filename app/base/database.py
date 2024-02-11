# external imports
import fastapi
import sqlite3
from datetime import datetime, timedelta
# internal imports
from ..utils.constants import (
    DATABASE_LOCATION
)


class Database:
    def __init__(self):
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS cache (ip TEXT PRIMARY KEY, details TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    @property
    def connection(self):
        return sqlite3.connect(DATABASE_LOCATION)

    def get_row_by_ip(self, ip: str):
        result = self.connection.execute(
            "SELECT * FROM cache WHERE ip = ?", (ip,)).fetchone()
        return result

    def get_all_ips(self) -> list:
        cursor = self.connection.execute("SELECT * FROM cache")
        return cursor.fetchall()

    def save_ipinfo_location(self, ip: str, details: str):
        conn = self.connection
        conn.execute(
            "INSERT INTO cache (ip, details) VALUES (?, ?)", (ip, details)
        )
        conn.commit()
        conn.close()
