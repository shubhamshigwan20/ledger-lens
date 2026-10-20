from fastapi import FastAPI, APIRouter
from datetime import datetime, timezone
from utils.dependancies import db_dependancy
from sqlalchemy import text

app = FastAPI()
router = APIRouter()

@router.get('/')
async def health_check(db : db_dependancy):
    result = db.execute(text("SELECT 1"))
    print(f"db_status: {result}")

    return { 'service': 'backend', 'datetime': datetime.now(timezone.utc), 'status': True}


app.include_router(router)