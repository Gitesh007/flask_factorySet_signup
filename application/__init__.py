"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all


db = SQLAlchemy()
patch_all()


def create_app():
    """Construct the core application."""

    app = Flask(__name__, instance_relative_config=False)

    if app.config['ENV'] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config['ENV'] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app