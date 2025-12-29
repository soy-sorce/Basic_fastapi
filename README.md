# Basic_fastapi
This repository contains a minimal FastAPI project that demonstrates object-oriented code structure and a regex-based language detector.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.app:app --reload
```

## Run with Docker

```bash
docker build -t basic-fastapi .
docker run -p 8000:8000 basic-fastapi
```

After starting the server, send a POST request to `http://localhost:8000/language` with a JSON body such as:

```json
{
  "query": "こんにちは"
}
```
