FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system dependencies for postgres + mysql
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire Flask app
COPY . .

EXPOSE 8002

# Run with YOUR intentional --noreload flag
CMD ["gunicorn", "wsgi:application", "--bind", "0.0.0.0:8002", "-noreload"]
