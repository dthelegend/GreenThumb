from fastapi import APIRouter
from green_thumb.api.v1 import plant

router = APIRouter(prefix="/v1")

router.include_router(plant.router)