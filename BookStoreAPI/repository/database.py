from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from BookStoreAPI.models import Author
from BookStoreAPI.models.Book import Book


async def init_db():
    try:
        uri = r"mongodb://localhost:27017/"
        client = AsyncIOMotorClient(uri)
        database = client.get_database("Bookstore")
        await init_beanie(database=database, document_models=[Book, Author])
    except Exception as e:
        print("Error initializing database:", e)
