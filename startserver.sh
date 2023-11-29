# railway.run.sh

# Executa as migrações do banco de dados usando Alembic
alembic upgrade head

# Inicia o servidor da aplicação usando Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload