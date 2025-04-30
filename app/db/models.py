from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Desk(Base):
    __tablename__ = 'desks'

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    features = Column(String)
    vergesense_area_id = Column(String, ForeignKey('occupancy_data.area_id'))

    occupancy_data = relationship("OccupancyData", back_populates="desks")

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    preferences = Column(String)

class OccupancyData(Base):
    __tablename__ = 'occupancy_data'

    id = Column(Integer, primary_key=True, index=True)
    area_id = Column(String, index=True)
    current_occupancy = Column(Integer)

    desks = relationship("Desk", back_populates="occupancy_data")