from fastapi import FastAPI
from dotenv import load_dotenv
from controllers.post_controller import router
from database import database, metadata, engine
load_dotenv('.env')  

app = FastAPI()

app.include_router(router, prefix="/CRUD")

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)

@app.on_event("startup")
def create_tables():
    metadata.create_all(engine)