from fastapi import FastAPI
import uvicorn
import threading
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine
from green_thumb import api

# =========== API ===========
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

@app.get("/")
def index():
    return RedirectResponse("https://www.youtube.com/watch?v=xvFZjo5PgG0")

def app():
    uvicorn.run(app)

# =========== LORAX ===========

def lorax():
    pass

# =========== GATHER ===========

def gather():
    pass

# =========== MAIN ===========

def main():
    main_threads = [threading.Thread(app),
                    threading.Thread(lorax),
                    threading.Thread(gather)]
    
    for thread in main_threads:
        thread.start()
    for thread in main_threads:
        thread.join()

if __name__ == '__main__':
    main()
