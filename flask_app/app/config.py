import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)

POSTGRES = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "15432"),
    "user": os.getenv("POSTGRES_USER", "devuser"),
    "password": os.getenv("POSTGRES_PASSWORD", "devpass"),
    "db": os.getenv("POSTGRES_DB", "testdb"),
}

MYSQL = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": os.getenv("MYSQL_PORT", "13307"),
    "user": os.getenv("MYSQL_USER", "devuser"),
    "password": os.getenv("MYSQL_PASSWORD", "devpass"),
    "db": os.getenv("MYSQL_DB", "testdb"),
}

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:19092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "flask-demo-topic")
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 8002))

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{POSTGRES['user']}:{POSTGRES['password']}@"
    f"{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
)

SQLALCHEMY_BINDS = {
    "mysql_db": (
        f"mysql+pymysql://{MYSQL['user']}:{MYSQL['password']}@"
        f"{MYSQL['host']}:{MYSQL['port']}/{MYSQL['db']}"
    )
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
