from contextlib import asynccontextmanager
from src.users.tasks.models import Todo
from fastapi import FastAPI
from .db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="FastAPI Tutorial by OM",
    version="0.1.0",
    description="This is a tutorial for FastAPI",
    lifespan=lifespan
)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("APP STARTED")
    create_db_and_tables()
    yield