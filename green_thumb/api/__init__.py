from fastapi import APIRouter
from green_thumb.api import v1

router = APIRouter(prefix="/api")

router.include_router(v1.router)