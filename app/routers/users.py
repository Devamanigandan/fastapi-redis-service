from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from uuid import uuid4
import json

from app.core.database import user_profiles, redis_client
from app.models.users import UserProfile

CACHE_TTL=300

router = APIRouter(prefix='/user')

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_schema: UserProfile):
    try:
        user_schema = dict(user_schema)

        if user_profiles.find_one({'email': user_schema['email']}) is not None:
            return JSONResponse(status_code=400, content=jsonable_encoder({"detail": 'Email is already exists'}))
        if user_profiles.find_one({'phone': user_schema['phone']}) is not None:
            return JSONResponse(status_code=400, content=jsonable_encoder({"detail": 'Phone number is already exists'}))
        user_schema['_id'] = str(uuid4())
        user_profiles.insert_one(user_schema)

        return JSONResponse(status_code=201, content=jsonable_encoder({"detail": 'User profile successfully created'}))
    except Exception as e:
        return JSONResponse(status_code=500, content=jsonable_encoder({"detail":str(e)}))
    
@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id: str):
    try:
        cached_details = await redis_client.get(id)
        if cached_details:
            return JSONResponse(status_code=200, content=jsonable_encoder({"detail": json.loads(cached_details)}))
        user_details = user_profiles.find_one({'_id': id})
        if not user_details:
            return JSONResponse(status_code=404, content=jsonable_encoder({"detail": 'Invalid user id'}))
        
        await redis_client.set(id, json.dumps(user_details), ex=CACHE_TTL)
        return JSONResponse(status_code=200, content=jsonable_encoder({"detail": user_details}))

    except Exception as e:
        return JSONResponse(status_code=500, content=jsonable_encoder({"detail":str(e)}))

