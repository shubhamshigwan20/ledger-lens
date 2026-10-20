from sqlalchemy import Column, String, Integer, DateTime, func
from db.base import Base
from sqlalchemy.dialects.postgresql import JSONB

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String[250], unique=True, nullable=False)
    hashed_password = Column(String[250], nullable=False)
    full_name = Column(String[150], nullable=False)
    preferences = Column(JSONB, default={}, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default= func.now(), nullable=False)
