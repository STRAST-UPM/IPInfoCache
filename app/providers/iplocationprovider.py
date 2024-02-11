# external imports
from datetime import datetime, timedelta
import ipinfo
import json
# internal imports
from ..base.database import Database
from ..models.ipinfo_locations import IPInfoLocation


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
            return self.update_ip_location(ip).to_dict()

    def update_ip_location(self, ip: str) -> IPInfoLocation:
        # location_info = self.request_to_ipinfo(ip)
        location_info = "location_info"
        self._db.save_ipinfo_location(
            ip, location_info
        )
        ip_row_data = self._db.get_row_by_ip(ip)
        item = IPInfoLocation(ip_row_data)
        return item

    def request_to_ipinfo(self, ip: str) -> str:
        access_token = "token"
        handler = ipinfo.getHandler(access_token)
        return json.dumps(handler.getDetails(ip).all)

