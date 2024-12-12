from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings
import logging


class MongoDB:
    client = None
    db = None

    @classmethod
    async def connect_to_database(cls):
        logging.info("Connecting to MongoDB...")
        try:
            cls.client = AsyncIOMotorClient(settings.MONGODB_URL)
            cls.db = cls.client[settings.DB_NAME]
            logging.info("Connected to MongoDB!")
            # Ping the database to verify connection
            await cls.db.command("ping")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise

    @classmethod
    async def close_database_connection(cls):
        logging.info("Closing MongoDB connection...")
        if cls.client:
            cls.client.close()
            logging.info("MongoDB connection closed!")

    @classmethod
    def get_db(cls):
        return cls.db


async def get_database():
    return MongoDB.get_db()
