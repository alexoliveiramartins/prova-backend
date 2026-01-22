from fastapi import APIRouter
from src.service.classificationService import classify
from src.models.message import Message

router = APIRouter(prefix="/classification", tags=["classification"])

@router.post("/")
async def classification(message: Message):
    response = classify(message.text)
    return {"classification": response}