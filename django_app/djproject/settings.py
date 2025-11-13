import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # DRF + OpenAPI
    "rest_framework",
    "drf_spectacular",

    # local app
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": ["django.template.context_processors.debug",
                                           "django.template.context_processors.request",
                                           "django.contrib.auth.context_processors.auth",
                                           "django.contrib.messages.context_processors.messages",],},
    },
]

WSGI_APPLICATION = "djproject.wsgi.application"

# Databases - default Postgres for User, mysql_db for Products
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "testdb"),
        "USER": os.getenv("POSTGRES_USER", "devuser"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "devpass"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "15432"),
    },
    "mysql_db": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": os.getenv("MYSQL_DB", "testdb"),
    "USER": os.getenv("MYSQL_USER", "devuser"),
    "PASSWORD": os.getenv("MYSQL_PASSWORD", "devpass"),
    "HOST": os.getenv("MYSQL_HOST", "localhost"),
    "PORT": os.getenv("MYSQL_PORT", "13307"),
    "OPTIONS": {
        "charset": "utf8mb4",
        "use_unicode": True,
    },
},
}

DATABASE_ROUTERS = ["djproject.db_router.DatabaseRouter"]

# Password validation (defaults)
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

# DRF & drf-spectacular config
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Django Demo API",
    "DESCRIPTION": "CRUD (Postgres/MySQL), Kafka publishing, external API",
    "VERSION": "1.0.0",
}
