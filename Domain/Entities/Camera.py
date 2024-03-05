from typing import Any
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .Base import Base


class Camera(Base):
    __tablename__ = 'camera'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    ip = Column(String(20), nullable=False)
    port = Column(Integer, nullable=False)
    password = Column(String(10), nullable=False)
    user = Column(String(10), nullable=False)
    manufacturer = Column(String(20), nullable=False)

    def __init__(self, user, password, ip, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.user = user
        self.password = password
