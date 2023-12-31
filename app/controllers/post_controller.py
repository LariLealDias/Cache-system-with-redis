from fastapi import APIRouter, HTTPException
from models.schemas.post_schema import PostBase, PostBaseToUpdate
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

        resultadoRedis = redis_client.setex(f"post_id:{last_record_id}", 21600, json.dumps(post_data.dict()))
        print(resultadoRedis)

        return {**post_data.dict(), "id": last_record_id}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"{e}Algo deu errado")

@router.get("/{post_id}")
async def get_one_post(post_id: int):
    try:
        get_cached_post = redis_client.get(f"post_id:{post_id}")

        if get_cached_post:
            deserialized_cached_post = json.loads(get_cached_post)
            return deserialized_cached_post
        
        query = post.select().where(post.c.id == post_id)
        post_data = await database.fetch_one(query)
       
        if post_data:
            data = {
                "title": post_data.title,
                "text": post_data.text,
            }
            
            redis_client.setex(f"post_id:{post_id}", 21600, json.dumps(data))
            return data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Algo deu errado")

@router.patch('/{post_id}')
async def update_post_by_id(post_id: int, update_data: PostBaseToUpdate):
    try:
        query = post.update().where(post.c.id == post_id).values(title=update_data.title, text=update_data.text)
        result = await database.execute(query)

        if result:
            updated_query = post.select().where(post.c.id == post_id)
            updated_post = await database.fetch_one(updated_query)

            if updated_post:
                data = {
                    "title": updated_post.title,
                    "text": updated_post.text,
                }
                
                redis_client.setex(f"post_id: {post_id}", 21600, json.dumps(data))
                return data

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Algo deu errado")   

@router.delete("/{post_id}")
async def delete_post(post_id: int):
    try:
        query = post.delete().where(post.c.id == post_id)
        result = await database.execute(query)

        if result:
            redis_client.delete(f"post_id:{post_id}")
            return {"message": "Postagem excluída com sucesso"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Algo deu errado")
