from pydantic import BaseModel

class PlantDataPointBase(BaseModel):
    temperature: float
    humidity: float
    light_level: int
    water_level: int

class PlantDataPoint(PlantDataPointBase):
    id: int
    plant_id: int

    class Config:
        from_attributes = True

class PlantBase(BaseModel):
    name: str
    description: str

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    id: int

class PlantList(PlantBase):
    id: int
    latest_data: PlantDataPointBase

    class Config:
        from_attributes = True

class Plant(PlantBase):
    id: int
    data: list[PlantDataPoint] = []

    class Config:
        from_attributes = True
