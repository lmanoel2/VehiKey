from typing import Any
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from .Base import Base


class Camera(Base):
    __tablename__ = 'camera'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    ip = Column(String(20), nullable=False)
    port = Column(Integer, nullable=False)
    password = Column(String(10), nullable=False)
    user = Column(String(10), nullable=False)
    name = Column(String(30), nullable=False)
    manufacturer = Column(String(20), nullable=False)
    valid_time = Column(String(50), nullable=True)

    def __init__(self, user: str = None, password: str = None, ip: str = None, name: str = 'default',                 manufacturer: str = 'unknown', port: int = 80):
        if user is not None and password is not None and ip is not None:
            self.user = user
            self.password = password
            self.ip = ip
            self.name = name
            self.manufacturer = manufacturer
            self.port = port

    def SetValidTime(self, validTime: str):
        self.valid_time = validTime

    def GetValidTime(self):
        if not self.valid_time:
            return None, None

        startDate, endDate = self.valid_time.split()
        start = datetime.strptime(startDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)
        end = datetime.strptime(endDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)

        return start, end

    def GetManufacturer(self):
        return self.manufacturer

    def GetName(self):
        return self.name

    def GetUser(self):
        return self.user

    def GetPassword(self):
        return self.password

    def GetPort(self):
        return self.port

    def GetIp(self):
        return self.ip