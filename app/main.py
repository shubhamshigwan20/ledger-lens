from fastapi import FastAPI, APIRouter
from datetime import datetime, timezone
from utils.dependancies import db_dependancy
from sqlalchemy import text
from db.base import Base
from db.session import engine
from models import users, transactions, categories, budgets

app = FastAPI()
router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get('/')
async def health_check(db : db_dependancy):
    result = db.execute(text("SELECT 1"))
    print(f"db_status: {result}")

    return { 'service': 'backend', 'datetime': datetime.now(timezone.utc), 'status': True}


app.include_router(router)