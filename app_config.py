from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL

# Returns app config.
def get_app_config():

    # App start.
    app = Flask(__name__)

    # Config MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'myflaskapp'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['MYSQL_PORT'] = 3300

    return app
