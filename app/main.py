# external imports
import fastapi
import sqlite3
from datetime import datetime, timedelta
# internal imports
from app.base.database import Database
from app.models.ipinfo_locations import IPInfoLocation
from app.providers.iplocationprovider import IPLocationProvider

app = fastapi.FastAPI()

db = Database()
ip_location_provider = IPLocationProvider(db)


@app.get("/ip/{ip}")
def get_ip(ip: str):
    return ip_location_provider.get_ip_location(ip)


@app.get("/ip_all")
def get_all_ip():
    rows = db.get_all_ips()
    return [IPInfoLocation(row).to_dict() for row in rows]
