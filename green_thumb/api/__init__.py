from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from green_thumb import api
from fastapi import APIRouter
from green_thumb.api import v1

# =========== API ===========
api = FastAPI()

origins = [
    "*"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api")

router.include_router(v1.router)

api.include_router(router)

@api.get("/")
def index():
    return RedirectResponse("https://www.youtube.com/watch?v=xvFZjo5PgG0")

def main():
    print("Running API...")
    uvicorn.run(api)

if __name__ == '__main__':
    main()
