import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"))
db = client[os.getenv("MONGODB_DBNAME")]
notes_collection = db["notes"]
