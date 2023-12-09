from fastapi import FastAPI
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData
from models.schemas.post_schema import PostBase
from models.model.post_model_db import post
from databases import Database

load_dotenv('.env')  

DATABASE_URL = os.getenv("DATABASE_URL")
metadata = MetaData()
engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/create-post/")
async def create_post(post_data: PostBase):
    query = post.insert().values(title=post_data.title, text=post_data.text)
    last_record_id = await database.execute(query)
    return {**post_data.dict(), "id": last_record_id}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def create_tables():
    metadata.create_all(engine)