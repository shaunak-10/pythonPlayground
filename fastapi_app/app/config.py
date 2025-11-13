from pydantic import BaseSettings

class Settings(BaseSettings):
    # Postgres
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 15432
    POSTGRES_USER: str = "devuser"
    POSTGRES_PASSWORD: str = "devpass"
    POSTGRES_DB: str = "testdb"

    # MySQL
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 13307
    MYSQL_USER: str = "devuser"
    MYSQL_PASSWORD: str = "devpass"
    MYSQL_DB: str = "testdb"

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:19092"
    KAFKA_TOPIC: str = "fastapi-demo-topic"

    FASTAPI_HOST: str = "0.0.0.0"
    FASTAPI_PORT: int = 8000

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

settings = Settings()
