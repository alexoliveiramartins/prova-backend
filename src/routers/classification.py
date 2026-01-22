from fastapi import APIRouter
from openai import OpenAI
from src.models.classificationResponse import ClassificationResponse
from src.service.classificationService import classify, classifyLLM
from src.models.message import Message

router = APIRouter(prefix="/classification", tags=["classification"])

@router.post("/simple")
async def classification(message: Message, response_model=ClassificationResponse):
    response = classify(message.text)
    return {"Classificacao": response}

@router.post("/llm")
async def classification(message: Message, response_model=ClassificationResponse):
    response = classifyLLM(message.text)
    return {"Classificacao": response}