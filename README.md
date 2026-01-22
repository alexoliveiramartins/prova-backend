# prova-backend

Aplicativo de classificação simples de textos com uso de Heurísticas ou por meio de LLMs

- Classificação heurística baseada em palavras-chave
- Classificação via LLMs 

# Pré Requisitos

- Python 3
- pip
- Conta HuggingFace (opcional)

# Como rodar

```bash
# Criar o ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn src.main:app --reload
```

A API estará disponível em:
http://127.0.0.1:8000

# (Opcional) Configurar a chave de API do HuggingFace

1. Criar conta no HuggingFace
2. Ir em https://huggingface.co/settings/tokens > Create new token > Selecionar "Fine Grained"
3. Marcar "Make calls to Inference Providers" na seção de "Inference"
4. Criar um arquivo `.env` na raiz do projeto e colar o token da forma que está no arquivo `.env.example`

# Exemplos de requisições

## Endpoint de classificação simples com Heurísticas (/classification/simple)

```bash
curl --location 'http://127.0.0.1:8000/classification/simple' \
    --header 'Content-Type: application/json' \
    --data '{
        "text": "Produto ótimo"
    }'
```

Saída esperada:

```json
{
    "Classificacao": {
        "Categoria": "Positivo",
        "Sentimento": "Positivo",
        "Confianca": 0.75
    }
}
```

---

```bash
curl --location 'http://127.0.0.1:8000/classification/simple' \
    --header 'Content-Type: application/json' \
    --data '{
        "text": "Produto péssimo"
    }'
```

Saída esperada:

```json
{
    "Classificacao": {
        "Categoria": "Negativo",
        "Sentimento": "Negativo",
        "Confianca": 0.75
    }
}
```

---

```bash
curl --location 'http://127.0.0.1:8000/classification/simple' \
    --header 'Content-Type: application/json' \
    --data '{
        "text": "Qual o valor?"
    }'
```

Saída esperada:

```json
{
    "Classificacao": {
        "Categoria": "Questao",
        "Sentimento": "Questao",
        "Confianca": 0.75
    }
}
```

## Endpoint de classificação com LLMs (/classification/llm)

```bash
curl --location 'http://127.0.0.1:8000/classification/llm' \
    --header 'Content-Type: application/json' \
    --data '{
        "text": "Qual o valor?"
    }'
```

Saída esperada:

```json
{
    "Classificacao": {
        "Categoria": "Question",
        "Sentimento": "Neutral",
        "Confianca": 0.95
    }
}
```

# Documentação da API

Redoc:
http://127.0.0.1:8000/redoc

Swagger:
http://127.0.0.1:8000/docs
