import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

negative_words = ["ruim", "péssimo", "odeio", "odiei", "desapontado", "decepção"]
positive_words = ["bom", "ótimo", "amei"]
 
def classify(message: str):
    message_words = message.lower().split()
    if '?' in message:
        return "Question"
    elif any(word in message_words for word in negative_words):
        return "Negative"
    elif any(word in message_words for word in positive_words):
        return "Positive"
    else: return "null"

def classifyLLM(message: str):
    client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
    )

    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[
            {
                "role": "user",
                "content": f"Classify this text in a simple category, send only the category name: {message}"
            }
        ],
    )

    print(completion.choices[0].message)
    return completion.choices[0].message.content