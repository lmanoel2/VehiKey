from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .Base import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    message = Column(String(600), nullable=True)

    def __init__(self, message):
        self.message = message
