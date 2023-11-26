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

    base_water_level: int # This is the water level when dry!    
    water_min: int # How much water is needed in 24h period
    water_max: int # How much water is needed to drown the plant

    light_requirment: int # How much light is needed in 24h period

    min_temperature: int
    max_temperature: int
    min_humididty: float
    max_humididty: float

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
