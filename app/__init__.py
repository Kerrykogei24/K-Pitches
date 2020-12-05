from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from confign import config_options

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initializing flask extensions
    db.init_app(app)


    return app