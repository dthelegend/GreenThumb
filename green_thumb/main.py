from fastapi import FastAPI
import uvicorn
import threading
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine
from green_thumb import api
from green_thumb.db import get_db_scoped
from green_thumb.db.models import Plant
from green_thumb.lorax import e2e_interact
from time import sleep as zzz

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

api.include_router(api.router)

@api.get("/")
def index():
    return RedirectResponse("https://www.youtube.com/watch?v=xvFZjo5PgG0")

def api():
    print("Running API...")
    uvicorn.run(api)

# =========== LORAX ===========

def lorax():
    print("Running Lorax...")
    while True:
        print("loraxxxxxx")
        e2e_interact()
        zzz(5)

# =========== MAIN ===========

def main():
    main_threads = [threading.Thread(api),
                    threading.Thread(lorax)]
    
    for thread in main_threads:
        thread.start()
    for thread in main_threads:
        thread.join()

if __name__ == '__main__':
    main()
