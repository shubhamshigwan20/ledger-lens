from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, Date, func
from db.base import Base

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='RESTRICT'), nullable=False)
    amount = Column(Numeric(12,2), nullable=False)
    description = Column(String(255), nullable=False)
    merchant = Column(String(255))
    occurred_on = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())