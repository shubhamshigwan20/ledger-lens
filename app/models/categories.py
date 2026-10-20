from sqlalchemy import Column,Integer,  String, ForeignKey, UniqueConstraint
from db.base import Base

class Categories(Base):
    __tablename__ = 'categories'

    __table_args__ = (UniqueConstraint('user_id', 'name', name='uq_categories_user_id_name'),)

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(150), nullable=False)
