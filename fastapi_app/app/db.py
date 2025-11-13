from sqlalchemy import (
    MetaData, Table, Column, Integer, String, Float
)
from sqlalchemy import create_engine
from databases import Database
from .config import settings

# Postgres (Users)
PG_DSN = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

# MySQL (Products)
MYSQL_DSN = f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}"

# databases.Database instances (async)
database_pg = Database(PG_DSN)
database_mysql = Database(MYSQL_DSN)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("price", Float, nullable=False),
)

# traditional engines for metadata create
engine_pg = create_engine(PG_DSN)
engine_mysql = create_engine(MYSQL_DSN)
