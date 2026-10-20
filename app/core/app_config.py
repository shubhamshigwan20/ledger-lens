import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / '.env')

DB_URL = os.getenv('DB_URL')
if not DB_URL:
    raise RuntimeError(
        f'DB_URL is not configured. Add DB_URL to {BASE_DIR / ".env"} '
        'or set it as an environment variable.'
    )
