# external imports
from datetime import datetime, timedelta
import ipinfo
import json
import dotenv
from os import getenv
# internal imports
from ..base.database import Database
from ..models.ipinfo_locations import IPInfoLocation
from ..utils.constants import (
    ENV_PATH
)


class IPLocationProvider:
    def __init__(self, db: Database,
                 ipinfo_token: str = "token"):
        self._db = db
        self._ipinfo_token = ipinfo_token

    def get_ip_location(self, ip: str) -> dict:
        row = self._db.get_row_by_ip(ip)
        if row is not None:
            item = IPInfoLocation(row)
            if item.created_at < datetime.now() - timedelta(days=30):
                return self.update_ip_location(ip).to_dict()
            else:
                return item.to_dict()
        else:
            return self.insert_ip_location(ip).to_dict()

    def update_ip_location(self, ip: str) -> IPInfoLocation:
        self.remove_ip_location(ip)
        item = self.insert_ip_location(ip)
        return item

    def insert_ip_location(self, ip: str) -> IPInfoLocation:
        location_info = self.request_to_ipinfo(ip)
        self._db.save_ipinfo_location(
            ip, location_info
        )
        ip_row_data = self._db.get_row_by_ip(ip)
        item = IPInfoLocation(ip_row_data)
        return item

    def remove_ip_location(self, ip: str):
        self._db.delete_ipinfo_location(ip)

    def request_to_ipinfo(self, ip: str) -> str:
        dotenv.load_dotenv(ENV_PATH)
        access_token = getenv("IPINFO_TOKEN")
        handler = ipinfo.getHandler(access_token)
        return json.dumps(handler.getDetails(ip).all)

