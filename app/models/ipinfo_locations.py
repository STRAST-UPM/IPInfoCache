# external imports
from datetime import datetime
# internal imports


class IPInfoLocation:
    def __init__(self, db_row):
        self._ip = db_row[0]
        self._details = db_row[1]
        self._created_at = datetime.strptime(db_row[2], "%Y-%m-%d %H:%M:%S")

    @property
    def ip(self):
        return self._ip

    @property
    def details(self):
        return self._details

    @property
    def created_at(self):
        return self._created_at

    def to_dict(self) -> dict:
        return {
            "ip": self._ip,
            "details": self._details,
            "created_at": str(self._created_at)
        }
