from typing import List

from click import INT
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, relationship, mapped_column
from sqlalchemy.sql import func
from green_thumb.common.db import engine

Base = declarative_base()

class Plant(Base):
    __tablename__ = "plant_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

    base_water_level = Column(Integer) # This is the water level when dry!    
    water_min = Column(Integer) # How much water is needed in 24h period
    water_max = Column(Integer) # How much water is needed to drown the plant

    light_requirment = Column(Integer) # How much light is needed in 24h period

    min_temperature = Column(Float)
    max_temperature = Column(Float)
    min_humididty = Column(Float)
    max_humididty  = Column(Float)

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