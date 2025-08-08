FROM python:3.11-slim

WORKDIR /code

# system deps (optional) for building psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# default command is handled by docker-compose (safer), so we leave CMD optional
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 3698 --reload"]
