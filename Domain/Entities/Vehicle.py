from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .Base import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    model = Column(String(20), nullable=True)
    color = Column(String(10), nullable=True)
    plate = Column(String(10), nullable=False)

