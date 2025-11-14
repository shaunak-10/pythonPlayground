FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# System deps for postgres + mysql
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY . .

# Expose Django port
EXPOSE 8001

# Run with YOUR intentional flag
CMD ["gunicorn", "djproject.wsgi:application", "--bind", "0.0.0.0:8001", "-noreload"]
