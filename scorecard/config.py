"""Configuration settings for the Scorecard service."""

import os

from flask import current_app


class Config(object):
    """The default application configuration."""

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # https://flask-jwt-extended.readthedocs.io/en/stable/options/
    JWT_TOKEN_LOCATION = "cookies"
    JWT_ALGORITHM = "RS256"
    JWT_PUBLIC_KEY = open("keys/heimdall.pub").read()
    JWT_IDENTITY_CLAIM = "sub"
    JWT_ACCESS_COOKIE_PATH = "/"
    JWT_REFRESH_COOKIE_PATH = "/refresh"
    JWT_COOKIE_DOMAIN = os.getenv("JWT_COOKIE_DOMAIN", None)
    JWT_COOKIE_SECURE = os.getenv("JWT_COOKIE_SECURE", False)
    JWT_ACCESS_CSRF_COOKIE_PATH = "/"
    JWT_REFRESH_CSRF_COOKIE_PATH = "/"


class TestConfig(Config):
    """The application configuration for testing."""

    # Make sure the application's instance folder exists
    os.makedirs(current_app.instance_path, exist_ok=True)

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(current_app.instance_path, "db.sqlite3")

    JWT_COOKIE_SECURE = False
