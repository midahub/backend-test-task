from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

from config import settings
from core.database.models import MODELS


async def initialize_database():
    try:
        client = AsyncIOMotorClient(settings.MONGODB_URL)
        await init_beanie(database=client.ContentMicroservice, document_models=MODELS)
    except ConnectionFailure as e:
        raise e
