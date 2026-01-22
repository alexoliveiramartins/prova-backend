from fastapi import APIRouter
from openai import OpenAI
from src.service.classificationService import classify, classifyLLM
from src.models.message import Message

router = APIRouter(prefix="/classification", tags=["classification"])

@router.post("/simple")
async def classification(message: Message):
    response = classify(message.text)
    return {"classification": response}

@router.post("/llm")
async def classification(message: Message):
    response = classifyLLM(message.text)
    return {"classification": response}