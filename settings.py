import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "fast_api_tut")
    db_driver = os.getenv("DB_DRIVER", "mysql+mysqlconnector")

    if not db_username or not db_password:
        raise RuntimeError("DATABASE_URL or DB_USERNAME and DB_PASSWORD must be set in the environment or .env")

    encoded_password = quote_plus(db_password)
    DATABASE_URL = f"{db_driver}://{db_username}:{encoded_password}@{db_host}:{db_port}/{db_name}"


class Settings:
    DATABASE_URL = DATABASE_URL


settings = Settings()