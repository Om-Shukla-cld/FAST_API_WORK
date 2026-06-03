from dotenv import load_dotenv
from src.users.tasks.models import Todo
import os
from urllib.parse import quote_plus

load_dotenv()
from sqlmodel import create_engine, SQLModel

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "fast_api_tut")
DB_DRIVER = os.getenv("DB_DRIVER", "mysql+mysqlconnector")

if not DB_USERNAME or not DB_PASSWORD:
    raise RuntimeError("DB_USERNAME and DB_PASSWORD must be set in the environment or .env")

encoded_password = quote_plus(DB_PASSWORD)
DB_URL = f"{DB_DRIVER}://{DB_USERNAME}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

from sqlalchemy import create_engine

engine = create_engine(
    DB_URL,
    echo=True
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)