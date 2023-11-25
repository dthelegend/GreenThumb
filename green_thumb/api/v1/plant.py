from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import green_thumb.db as db
import green_thumb.db.models as models
import green_thumb.db.schemas as schemas

router = APIRouter(prefix="/plants")

@router.get("/list")
async def read_plant_list(database: Session = Depends(db.get_db)) -> list[schemas.Plant]:
    plants = database.query(models.Plant).all()
    return plants

@router.get("/{plant_id}")
async def read_plant_by_id(plant_id: int, database: Session = Depends(db.get_db)) -> schemas.Plant:
    plant = database.query(models.Plant).get(plant_id)

    print("hi")
    if plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")

    return plant

@router.post("")
async def create_plant(plant: schemas.PlantCreate, database: Session = Depends(db.get_db)) -> schemas.Plant:
    database.add(**plant)
    database.commit()
    database.refresh(plant)
    return plant

@router.post("/{plant_id}")
async def update_plant_by_id(plant_id: int, plant: schemas.PlantUpdate, database: Session = Depends(db.get_db)) -> schemas.Plant:
    if plant.id != plant_id:
        raise HTTPException(status_code=401, detail="Plant ids in request do not match")

    plant_fetched = database.query(models.Plant).get(plant_id)

    if plant_fetched is None:
        raise HTTPException(status_code=404, detail="Plant not found")
    
    plant_fetched.update(**plant)

    database.add(plant_fetched)
    database.commit()
    database.refresh(plant_fetched)

    return plant_fetched