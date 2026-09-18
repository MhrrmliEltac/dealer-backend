import os
from typing import List

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def database_url() -> str:
    if url := os.getenv("DATABASE_URL"):
        return url
    if os.getenv("VERCEL") == "1":
        return "sqlite:////tmp/db.sqlite3"
    return "sqlite://db.sqlite3"


def tortoise_config(app: FastAPI, models: List["str"]):
    register_tortoise(
        app=app,
        db_url=database_url(),
        generate_schemas=True,
        modules={"models": models},
    )
