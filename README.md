# prova-backend

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

# Documentação da API

Redoc:
http://127.0.0.1:8000/redoc

Swagger:
http://127.0.0.1:8000/docs
