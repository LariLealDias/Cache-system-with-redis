from fastapi import APIRouter, HTTPException
from models.schemas.post_schema import PostBase
from models.model.post_model_db import post
import os
from dotenv import load_dotenv
from database import database

load_dotenv('.env')  

router = APIRouter()

@router.post("/create-post/")
async def create_post(post_data: PostBase):
    try:
        query = post.insert().values(title=post_data.title, text=post_data.text)
        last_record_id = await database.execute(query)
        return {**post_data.dict(), "id": last_record_id}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Algo deu errado")

@router.get("/")
def read_root():
    return {"Hello": "World"}
