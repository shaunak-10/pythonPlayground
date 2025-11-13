# Django App (django_app)

A minimal Django + DRF app demonstrating:
- CRUD for User (Postgres) and Product (MySQL) across two DBs
- Kafka publish endpoint + sample consumer script (kafka-python)
- External API proxy
- OpenAPI/Swagger via drf-spectacular
- Run with gunicorn (WSGI)

## Requirements
- Python 3.9+
- Docker & docker-compose (for Postgres/MySQL/Kafka) — use Docker Compose v2 (`docker compose`)
- This project uses environment variables (.env)

## Quick start (Linux / macOS)

1. Start external services (from repo root):
   docker compose up -d

2. Create & activate a virtualenv:
   cd django_app
   path/to/python -m venv venv
   source venv/bin/activate

3. Install pinned requirements:
   pip install -r requirements.txt

4. Copy example env:
   cp .env.example .env
   # edit .env if needed

5. Apply migrations:
   # make sure DBs are up (see docker compose)
   python manage.py makemigrations api
   python manage.py migrate --database=default
   python manage.py migrate --database=mysql_db


6. Run:
   linux: gunicorn djproject.wsgi:application --bind 0.0.0.0:8001 -noreload
   windows: python manage.py runserver 0.0.0.0:8001


7. Visit docs:
   Swagger UI: http://127.0.0.1:8001/api/schema/swagger-ui/
   OpenAPI JSON: http://127.0.0.1:8001/api/schema/

## Kafka
- Publish endpoint: POST /kafka/publish/ (JSON body)
- Consumer: run `python kafka_consumer.py` in the django_app venv in other terminal
- Topic default: from .env `KAFKA_TOPIC=django-demo-topic`. You can change it.

## Windows Notes
- Activate venv in PowerShell:
  venv\Scripts\Activate
- Run Docker Desktop (includes Compose v2)
- Use same steps after activating venv

## Database routing & notes
- `User` model uses the default DB (Postgres)
- `Product` model uses `mysql_db` (MySQL)
- The routing is implemented in `djproject/db_router.py`

## Endpoints (selected)
- /api/users/  (CRUD, Postgres)
- /api/products/ (CRUD, MySQL)
- /kafka/publish/ (POST) -> publishes to Kafka
- /external/jsonplaceholder/ -> proxy to a public API
- Swagger: /api/schema/swagger-ui/


after instrumentation, make sure to export DJANGO_SETTINGS_MODULE=djproject.settings

