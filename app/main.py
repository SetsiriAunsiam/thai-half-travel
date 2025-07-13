from fastapi import FastAPI

from .database import create_db_and_tables

from . import routers

app = FastAPI()

app.include_router(routers.router)

create_db_and_tables()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}