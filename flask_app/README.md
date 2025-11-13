# Flask App (flask_app)

Features:
- CRUD for User (Postgres) and Product (MySQL)
- Kafka publish endpoint + consumer script
- External API proxy
- Swagger UI at /docs (flask-restx)

Requirements:
- Python 3.9+
- Docker + docker-compose v2 (shared root docker-compose)
- Virtualenv per app recommended

Quick start (Linux/macOS):
1. Start infra: docker compose up -d
2. Create venv:
   cd flask_app
   path/to/python -m venv venv
   source venv/bin/activate
3. Install:
   pip install -r requirements.txt
4. Copy env:
   cp .env.example .env
5. Run:
   gunicorn wsgi:application --bind 0.0.0.0:8002 -noreload
6. Swagger UI:
   http://127.0.0.1:8002/docs

Kafka:
- POST /api/kafka/publish with JSON body like:
  {"message": {"hello": "world"}}
- Run consumer: python kafka_consumer.py

Notes:
- Tables auto-created by SQLAlchemy (db.create_all) on app startup (dev convenience)
- For production use, use proper migrations (Alembic) and manage sessions carefully
