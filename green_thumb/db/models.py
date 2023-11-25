from typing import List
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.sql import func
from green_thumb.db import Base
from datetime import datetime

class Plant(Base):
    __tablename__ = "plant_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(primary_key=True)
    data: Mapped[List["PlantDataPoint"]] = relationship(back_populates="plant")

class PlantDataPoint(Base):
    __tablename__ = "plant_data_point_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_created: Mapped[datetime] = mapped_column(server_default=func.now())
    plant: Mapped["Plant"] = relationship(back_populates="data")
    temperature: Mapped[float] = mapped_column()
    humidity: Mapped[float] = mapped_column()
    light_level: Mapped[int] = mapped_column()
    water_level: Mapped[int] = mapped_column()