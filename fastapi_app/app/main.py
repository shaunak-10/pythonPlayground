import asyncio
from fastapi import FastAPI
from .config import settings
from .db import database_pg, database_mysql, engine_pg, engine_mysql, metadata
from .routers import users, products, kafka as kafka_router, external as external_router
from . import db as dbmodule
import os

app = FastAPI(title="Demo FastAPI App - CRUD + Kafka + External API")

# include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(kafka_router.router)
app.include_router(external_router.router)

@app.on_event("startup")
async def startup():
    # load env from .env auto by pydantic in config.py
    # connect databases
    await database_pg.connect()
    await database_mysql.connect()

    # create tables if not present (sync create via engines)
    # NOTE: simple dev approach: create all metadata in both DBs
    dbmodule.metadata.create_all(bind=engine_pg)
    dbmodule.metadata.create_all(bind=engine_mysql)

@app.on_event("shutdown")
async def shutdown():
    await database_pg.disconnect()
    await database_mysql.disconnect()

@app.get("/")
async def root():
    return {"msg": "FastAPI demo (Users->Postgres, Products->MySQL). See /docs"}
