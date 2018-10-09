# coding: utf-8
# Python imports.
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Main app.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Setting up config.
app.config.from_pyfile("app_config.cfg")

# Database object.
db = SQLAlchemy(app)

# Login manager.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Local imports.
from app.blueprints import urls_blueprint

# Registering blueprints.
app.register_blueprint(urls_blueprint)

# Database initializer.
with app.app_context():
    db.init_app(app)
    db.create_all()
