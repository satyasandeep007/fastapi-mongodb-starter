from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    
async def get_database() -> AsyncIOMotorClient:
    return Database.client[os.getenv("DB_NAME")]

async def connect_to_mongo():
    print("Connecting to MongoDB...")
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    print(client)
    Database.client = client
    print("Connected to MongoDB")
    
async def close_mongo_connection():
    print("Closing MongoDB connection...")
    Database.client.close()
    print("MongoDB connection closed")