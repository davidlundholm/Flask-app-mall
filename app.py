# coding: utf-8
# Python imports.
from flask import Flask, render_template, request

# Local imports.
from models import db
from blueprints import urls_blueprint

# Main app.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Setting up config.
app.config.from_pyfile("app_config.cfg")

# Registering blueprints.
app.register_blueprint(urls_blueprint)

# Database initializer.
with app.app_context():
    db.init_app(app)
    db.create_all()
    
# Main start.
if __name__ == '__main__':
    app.run(debug = True)

