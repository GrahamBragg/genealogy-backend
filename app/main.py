from fastapi import FastAPI

from .config.config import initiate_database
from .routers import persons

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()

app.include_router(persons.router, prefix="/persons")

@app.get("/")
async def root():
    return {"message": "Hello World"}

