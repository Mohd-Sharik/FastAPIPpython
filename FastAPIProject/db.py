# db.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://sharikkhan9012:H78WuXGwxONveKf4@projectcrud.wfwxigx.mongodb.net"
client = AsyncIOMotorClient(MONGO_URL)
db = client["notes"]  # Replace with your DB name

def get_db():
    return db
