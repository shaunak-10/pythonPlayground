# FastAPI App (fastapi_app)

This FastAPI app demonstrates:
- CRUD for User (Postgres) and Product (MySQL)
- Kafka publish endpoint + sample consumer
- External HTTP API call example
- OpenAPI (Swagger) available at /docs and ReDoc at /redoc

## Requirements
- Python 3.9+
- Docker & docker-compose (to run Postgres/MySQL/Kafka)
- Recommended: run in a virtual environment per this repo structure

## Quick start (developer machine)
1. Start shared infra:
   - docker compose up -d

2. Create a venv and install:
   - cd fastapi_app
   - /path/to/python -m venv venv
   - source venv/bin/activate(linux)
   - venv\Scripts\activate(windows)
   - pip install -r requirements.txt

3. Configure env:
   - cp .env.example .env

4. Apply DB setup (the app auto-creates tables on first run). Just run the app.

5. Run app:
   - uvicorn app.main:app --host 0.0.0.0 --port 8000

6. Visit Swagger:
   - http://ip:8000/docs

## Endpoints (selected)
- POST /users/  (create user)            → Postgres
- GET /users/   (list users)
- GET /users/{id}
- PUT /users/{id}
- DELETE /users/{id}

- POST /products/ (create product)      → MySQL
- GET /products/

- POST /kafka/publish (publish message)
- GET /external/jsonplaceholder (proxy to JSONPlaceholder)

## Kafka consumer (example)
Run inside the venv in another terminal:
   python kafka_consumer.py

This will consume messages from the topic specified in .env.

## Notes
- DB and Kafka connection info come from environment variables (.env)
