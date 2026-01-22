from fastapi import FastAPI
from src.routers import classification

app = FastAPI()

app.include_router(classification.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}