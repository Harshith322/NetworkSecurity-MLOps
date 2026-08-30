import os
from pymongo import MongoClient

uri = os.getenv("MONGO_DB_URL")

if not uri:
    raise ValueError("MONGO_DB_URL environment variable is not set")

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("MongoDB connection successful!")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
finally:
    client.close()