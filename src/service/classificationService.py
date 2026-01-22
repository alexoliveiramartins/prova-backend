import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from openai import OpenAI
from src.models.classificationResponse import ClassificationResponse

load_dotenv()

keywords = {
    "negative_words": ["ruim", "péssimo", "odeio", "odiei", "desapontado", "decepção"],
    "positive_words": ["bom", "ótimo", "amei"]
}
 
def classify(message: str) -> ClassificationResponse:
    message_words = message.lower().split()
    if len(message) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo de texto nao deve ser vazio")
    elif '?' in message:
        return {
            "Categoria": "Questao",
            "Sentimento": "Questao",
            "Confianca": 0.75
        }
    elif any(word in message_words for word in keywords["negative_words"]):
        return {
            "Categoria": "Negativo",
            "Sentimento": "Negativo",
            "Confianca": 0.75
        }
    elif any(word in message_words for word in keywords["positive_words"]):
        return {
            "Categoria": "Positivo",
            "Sentimento": "Positivo",
            "Confianca": 0.75
        }
    else: return {
            "Categoria": "Outros",
            "Sentimento": "Neutro",
            "Confianca": 0.5
        }

def classifyLLM(message: str):
    if len(message) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo de texto nao deve ser vazio")
    elif not os.environ["HF_TOKEN"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chave de API nao encontrada")
    
    try:
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ["HF_TOKEN"],
        )

        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {
                    "role": "user",
                    "content": f"Answer in brazillian portuguese: Classify this text in a simple category, send only the category name (one word), the sentiment (positive, negative, neutral or question) and the classification confidence in the format 'Clasification Sentiment 0.00': {message}"
                }
            ],
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Erro no provedor da LLM")

    return {
        "Categoria": completion.choices[0].message.content.split()[0],
        "Sentimento": completion.choices[0].message.content.split()[1],
        "Confianca": float(completion.choices[0].message.content.split()[2])
    }