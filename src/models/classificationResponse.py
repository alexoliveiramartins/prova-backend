from pydantic import BaseModel

class ClassificationResponse(BaseModel):
    Categoria: str
    Sentimento: str
    Confianca: float