import os

# FILEPATHS
__APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
DATABASE_LOCATION = "/".join(__APP_DIR.split("/")[:-1]) + "/db/db.sqlite3"
