from fastapi import FastAPI
from typing import List
from tortoise.contrib.fastapi import register_tortoise


def tortoise_config(app: FastAPI, models: List["str"]):
    register_tortoise(
        app=app,
        db_url="sqlite://db.sqlite3",
        generate_schemas=True,
        modules={"models": models},
    )