from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import green_thumb.common.db as db
import green_thumb.common.db.models as models
import green_thumb.common.db.schemas as schemas

router = APIRouter(prefix="/plants")


@router.get("/list")
async def read_plant_data(
    database: Session = Depends(db.get_db),
) -> list[schemas.PlantList]:
    plants = list(
        schemas.PlantList(
            id=x.id,
            name=x.name,
            description=x.description,
            base_water_level=x.base_water_level,
            water_min=x.water_min,
            water_max=x.water_max,
            light_requirment=x.light_requirment,
            min_temperature=x.min_temperature,
            max_temperature=x.max_temperature,
            min_humididty=x.min_humididty,
            max_humididty=x.max_humididty,
            latest_data=None,  # TODO: Map this properly
        )
        for x in database.query(models.Plant).all()
    )
    return plants


@router.get("/{plant_id}")
async def read_plant_by_id(
    plant_id: int, database: Session = Depends(db.get_db)
) -> schemas.Plant:
    plant = database.query(models.Plant).get(plant_id)

    if plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")

    return plant


@router.post("")
async def create_plant(
    plant: schemas.PlantCreate, database: Session = Depends(db.get_db)
) -> schemas.Plant:
    plant_m = models.Plant(**plant.model_dump())
    try:
        database.add(plant_m)
    except IntegrityError as e:
        raise HTTPException(status_code=401, detail=e.detail)

    database.commit()
    database.refresh(plant_m)
    return plant_m


@router.post("/{plant_id}")
async def update_plant_by_id(
    plant_id: int, plant: schemas.PlantUpdate, database: Session = Depends(db.get_db)
) -> schemas.Plant:
    if plant.id != plant_id:
        raise HTTPException(status_code=401, detail="Plant ids in request do not match")

    plant_fetched = database.query(models.Plant).where(models.Plant.id == plant_id)

    rows_updated = plant_fetched.update(plant.model_dump())
    if rows_updated != 1:
        raise HTTPException(status_code=404, detail="Plant not found")

    database.commit()

    return database.query(models.Plant).get(plant_id)
