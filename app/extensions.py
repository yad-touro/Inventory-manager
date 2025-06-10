"""Flask extensions."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
cors = CORS()

# Configure login manager
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
login.login_message_category = 'info' 