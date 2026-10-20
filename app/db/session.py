from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from core.app_config import DB_URL

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
