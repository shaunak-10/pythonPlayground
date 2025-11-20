This SOP explains how to run all three applications — FastAPI, Django, and Flask — using Docker images provided as .tar files.
It includes:

Prerequisites

How to load Docker images

How to run each app normally

How to run each app with instrumentation

URLs to verify each service

📌 Prerequisites

Before running any application, ensure you are in the root directory of pythonPlayground.

Run the infrastructure stack:

docker compose up -d


This brings up Postgres, MySQL, Kafka, and other dependencies.

1. FastAPI Application
   
1.1 Load Image
   
docker load -i fastapi-app.tar

1.2 Normal Run

docker run \
  --env-file fastapi_app/.env.docker \
  --network=pythonplayground_default \
  -p 8000:8000 \
  fastapi-app

1.3 Instrumented Run

docker run -d \
  --add-host=host.docker.internal:host-gateway \
  -v "/motadata/motadata/config:/motadata/motadata/config" \
  -v "/motadata/motadata/instrumentation:/motadata/motadata/instrumentation" \
  --env-file fastapi_app/.env.docker \
  --network=pythonplayground_default \
  -p 8000:8000 \
  --entrypoint /bin/bash \
  fastapi-app \
  -c '. "/motadata/motadata/instrumentation/agents/python/python-instrumentation.sh" PythonFastAPIDoc && motadata-python-trace uvicorn app.main:app --host 0.0.0.0 --port 8000'

Verify

Visit: http://10.20.40.253:8000/docs

2. Django Application
2.1 Load Image
docker load -i django-app.tar

2.2 Normal Run
docker run \
  --env-file django_app/.env.docker \
  --network=pythonplayground_default \
  -p 8001:8001 \
  django-app

2.3 Instrumented Run
docker run -d \
  --add-host=host.docker.internal:host-gateway \
  -v "/motadata/motadata/config:/motadata/motadata/config" \
  -v "/motadata/motadata/instrumentation:/motadata/motadata/instrumentation" \
  --env-file django_app/.env.docker \
  --network=pythonplayground_default \
  -p 8001:8001 \
  --entrypoint /bin/bash \
  django-app \
  -c '. "/motadata/motadata/instrumentation/agents/python/python-instrumentation.sh" PythonDjangoDoc && motadata-python-trace gunicorn djproject.wsgi:application --bind 0.0.0.0:8001 -noreload'

Verify

Visit: http://10.20.40.253:8001/api/schema/swagger-ui/

3. Flask Application
3.1 Load Image
docker load -i flask-app.tar

3.2 Normal Run
docker run \
  --env-file flask_app/.env.docker \
  --network=pythonplayground_default \
  -p 8002:8002 \
  flask-app

3.3 Instrumented Run
docker run -d \
  --add-host=host.docker.internal:host-gateway \
  -v "/motadata/motadata/config:/motadata/motadata/config" \
  -v "/motadata/motadata/instrumentation:/motadata/motadata/instrumentation" \
  --env-file flask_app/.env.docker \
  --network=pythonplayground_default \
  -p 8002:8002 \
  --entrypoint /bin/bash \
  flask-app \
  -c '. "/motadata/motadata/instrumentation/agents/python/python-instrumentation.sh" PythonFlaskApp && motadata-python-trace gunicorn wsgi:application --bind 0.0.0.0:8002 -noreload'

Verify

Visit: http://10.20.40.253:8002/docs
