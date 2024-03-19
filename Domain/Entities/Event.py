from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

from typing_extensions import Any

from .Base import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    message = Column(String(600), nullable=True)
    sent_to_server = Column(Boolean, default=False, nullable=False)

    def __init__(self, message, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.message = message
