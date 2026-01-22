# prova-backend

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

# Documentação da API

Redoc:
http://127.0.0.1:8000/redoc

Swagger:
http://127.0.0.1:8000/docs
