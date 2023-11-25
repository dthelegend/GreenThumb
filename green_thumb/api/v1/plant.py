from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import green_thumb.db as db
import green_thumb.db.models as models
from sqlalchemy import select

router = APIRouter(prefix="/plants")

@router.get("/list")
async def read_plant_list(database: Session = Depends(db.get_db)):
    plants = database.query(models.Plant).all()
    return plants

@router.get("/get/{plant_id}")
async def read_plant_by_id(plant_id: int, database: Session = Depends(db.get_db)):
    plants = database.query(models.Plant).where(models.Plant.id.is_(plant_id))

    if len(plants) == 0:
        raise HTTPException(status_code=404, detail="Plant not found")

    return plants[0]
