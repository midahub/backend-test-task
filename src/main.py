from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import settings
from core.database.db import initialize_database


@asynccontextmanager
async def lifespan(application: FastAPI):
    await initialize_database()

    yield


app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_TITLE,
)

# TODO: Add routers here
ROUTERS = []

for router in ROUTERS:
    app.include_router(router)
