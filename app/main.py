# from fastapi import FastAPI
# from app.controllers.auth_controller import router
# app = FastAPI()

# app.include_router(router, prefix="/auth")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}