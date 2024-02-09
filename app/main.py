# external imports
import fastapi
import sqlite3
from datetime import datetime, timedelta
# internal imports
from base.database import Database
from models.ipinfo_locations import IPInfoLocation
from providers.iplocationprovider import IPLocationProvider

app = fastapi.FastAPI()

db = Database()
ip_location_provider = IPLocationProvider(db)


@app.get("/ip/{ip}")
def get_ip(ip: str):
    return ip_location_provider.get_ip_location(ip)


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
