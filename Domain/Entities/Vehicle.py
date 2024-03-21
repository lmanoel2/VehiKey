from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from .Base import Base


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    color = Column(String(10), nullable=True)
    plate = Column(String(10), nullable=False)
    valid_time = Column(String(50), nullable=True)  # '19-03-2024 00:00 25-03-2024 00:00'
    access_time = Column(String(500), nullable=True)
    number_access = Column(Integer, nullable=True)

    def SetColor(self, color: str):
        self.color = color

    def SetPlate(self, plate: str):
        self.plate = plate

    def SetValidTime(self, validTime: str):
        self.valid_time = validTime

    def SetAccessTime(self, accessTime: str):
        self.access_time = accessTime

    def SetNumberAccess(self, numberAccess: int):
        self.number_access = numberAccess

    def GetColor(self):
        return self.color

    def GetPlate(self):
        return self.plate

    def GetValidTime(self):
        if not self.valid_time:
            return None, None

        startDate, endDate = self.valid_time.split()
        start = datetime.strptime(startDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)
        end = datetime.strptime(endDate, "%d-%m-%Y-%H:%M").replace(tzinfo=timezone.utc)

        return start, end

    def GetAccessTime(self):
        return self.access_time

    def GetNumberAccess(self):
        return self.number_access
