from typing import List
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, relationship, mapped_column
from sqlalchemy.sql import func
from green_thumb.db import engine

Base = declarative_base()

class Plant(Base):
    __tablename__ = "plant_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    data: Mapped[List["PlantDataPoint"]] = relationship()

class PlantDataPoint(Base):
    __tablename__ = "plant_data_point_table"

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, server_default=func.now())
    plant_id = Column(ForeignKey("plant_table.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    light_level = Column(Integer)
    water_level = Column(Integer)


Base.metadata.create_all(engine)