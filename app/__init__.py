"""Flask application factory."""

import os
import logging
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import BaseConfig

from .extensions import cors
from .routes.main import main
from .routes.auth import auth
from .core.oauth import init_oauth
from .models.user import User

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_object=BaseConfig):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    cors.init_app(app)
    
    # Initialize OAuth
    init_oauth(app)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Initialize database
    with app.app_context():
        db.create_all()
        logger.info("Database tables created")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger.info("Application initialized")

    return app 
