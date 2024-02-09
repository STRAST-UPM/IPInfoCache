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
        self._connection = sqlite3.connect(DATABASE_LOCATION)

        # Creation of cache table
        self._connection.execute(
            "CREATE TABLE IF NOT EXISTS cache (ip TEXT PRIMARY KEY, details TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = sqlite3.connect(value)

    def get_row_by_ip(self, ip: str):
        return self._connection.execute(
            "SELECT * FROM cache WHERE ip = ?", (ip,)
        ).fetchone()

    def save_ipinfo_location(self, ip: str, details: str):
        self._connection.execute(
            "INSERT INTO cache (ip, value) VALUES (?, ?)", (ip, details)
        )

