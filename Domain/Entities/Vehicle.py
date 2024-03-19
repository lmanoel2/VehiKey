from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .Base import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    color = Column(String(10), nullable=True)
    plate = Column(String(10), nullable=False)
    valid_time = Column(String(50), nullable=True) #'19-03-2024 00:00 25-03-2024 00:00'
    access_time = Column(String(500), nullable=True)
    number_access = Column(Integer, nullable=True)

    def GetColor(self):
        return self.color

    def GetPlate(self):
        return self.plate

    def GetValidTime(self):
        if not self.valid_time:
            return None, None

        data_inicio, data_fim = self.valid_time.split()
        start = datetime.strptime(data_inicio, "%d-%m-%Y %H:%M")
        end = datetime.strptime(data_fim, "%d-%m-%Y %H:%M")

        return start, end

    def GetAccessTime(self):
        return self.access_time

    def get_number_access(self):
        return self.number_access
