from fastapi import APIRouter, HTTPException
from models.schemas.post_schema import PostBase
from models.model.post_model_db import post
import os
from dotenv import load_dotenv
from database import database
import redis
import json


load_dotenv('.env')  

redis_client = redis.Redis(host='localhost', port=6379, db=0)

router = APIRouter()

@router.post("/create-post/")
async def create_post(post_data: PostBase):
    try:
        query = post.insert().values(title=post_data.title, text=post_data.text)
        last_record_id = await database.execute(query)

        resultadoRedis = redis_client.set(f"post_id: {last_record_id}", json.dumps(post_data.dict()))
        print(resultadoRedis)

        return {**post_data.dict(), "id": last_record_id}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Algo deu errado")


