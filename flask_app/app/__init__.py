from flask import Flask
from flask_restx import Api
import app.config as config
from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS, SQLALCHEMY_TRACK_MODIFICATIONS, FLASK_HOST, FLASK_PORT
from .db import db
from .api_users import ns as users_ns
from .api_products import ns as products_ns
from .api_kafka import ns as kafka_ns
from .api_external import ns as external_ns
import os

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_BINDS"] = config.SQLALCHEMY_BINDS
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    api = Api(app, doc="/docs", title="Flask API", version="1.0")

    # Register Namespaces
    api.add_namespace(users_ns)
    api.add_namespace(products_ns)
    api.add_namespace(kafka_ns)
    api.add_namespace(external_ns)

    # Create tables (dev convenience)
    with app.app_context():
        # Create tables for default bind (users on Postgres)
        db.create_all()

        # Create tables for mysql bind
        from .models import Product
        engine_mysql = db.engines["mysql_db"]
        Product.__table__.create(bind=engine_mysql, checkfirst=True)

    return app


# for gunicorn import
app = create_app()
