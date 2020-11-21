"""Initialize the Scorecard service."""

import os

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .flask import Flask

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(config="scorecard.config.Config"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Manually push a context so the configuration has access to current_app
    with app.app_context():
        # Read in the application configuration
        app.config.from_object(config)

    # Enable CORS so the application can respond to requests from a subdomain
    CORS(app, origins=os.getenv("CORS_ORIGIN"), supports_credentials=True)

    _initialize_extensions(app)
    _register_blueprints(app)

    return app


def _initialize_extensions(app):
    # Initialize SQL alchemy and the migration engine
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize JSON web tokens
    jwt.init_app(app)


def _register_blueprints(app):
    from scorecard import exceptions, models, resources

    # Register the models blueprint
    app.register_blueprint(models.bp)

    # Register the exception handlers
    app.register_blueprint(exceptions.bp)

    # Register the application endpoints
    app.register_blueprint(resources.bp, url_prefix="/scorecard/v1")
