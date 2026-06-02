import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL must be set in the environment or in .env")


class Settings:
    DATABASE_URL = DATABASE_URL


settings = Settings()