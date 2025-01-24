from pymongo import MongoClient
from pymongo.collection import Collection
import redis.asyncio as redis

# MongoDB
client = MongoClient(host='localhost', port=27017)

user_profiles: Collection = client['fastapi-redis-service']['user_profiles']

# Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)