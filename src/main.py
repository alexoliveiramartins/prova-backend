from fastapi import FastAPI
from src.routers import classification, health

app = FastAPI()

app.include_router(classification.router)
app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}