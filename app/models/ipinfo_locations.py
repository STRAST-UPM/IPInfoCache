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

    @ip.setter
    def ip(self, value):
        self._ip = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    def to_dict(self) -> dict:
        return {
            "ip": self._ip,
            "details": self._details
        }
