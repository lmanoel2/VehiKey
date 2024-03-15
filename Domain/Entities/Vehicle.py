from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .Base import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    color = Column(String(10), nullable=True)
    plate = Column(String(10), nullable=False)
    valid_time = Column(String(50), nullable=True)
    access_time = Column(String(500), nullable=True)
    number_access = Column(Integer, nullable=True)
