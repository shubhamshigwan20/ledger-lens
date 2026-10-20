from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date, UniqueConstraint
from db.base import Base

class Budgets(Base):
    __tablename__ = 'budgets'

    __table_args__ = (UniqueConstraint('category_id', 'effective_from', name='uq_budgets_category_id_effective_from'),)

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer,ForeignKey('categories.id', ondelete='CASCADE'), nullable=False, )
    monthly_limit = Column(Numeric(12,2), nullable=False)
    effective_from = Column(Date, nullable=False)