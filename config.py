import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Log folder
LOG_FOLDER = "logs"

# Log file
LOG_FILE = "app.log"

# Default settings
DEFAULT_TOP_N = 1
