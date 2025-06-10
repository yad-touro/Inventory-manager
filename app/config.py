"""Application configuration."""

import os
from datetime import timedelta
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables from .env file
load_dotenv()

class BaseConfig:
    """Base configuration."""
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    FLASK_APP = os.environ.get("FLASK_APP", "run.py")
    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security
    SESSION_COOKIE_SECURE = True
    WTF_CSRF_ENABLED = True
    SESSION_LIFETIME = timedelta(hours=1)
    
    # Google OAuth
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    GOOGLE_SVC_KEY = os.environ.get("GOOGLE_SVC_KEY")
    
    # Frontend
    FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

    TWO_WAY_SYNC_ENABLED = os.getenv('TWO_WAY_SYNC_ENABLED', 'false').lower() == 'true'

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    WTF_CSRF_ENABLED = False

class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    WTF_CSRF_ENABLED = False
    TWO_WAY_SYNC_ENABLED = True

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    TESTING = False 