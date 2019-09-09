from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creation of the app configurations
    app.config.from_object(config_options[config_name])

    #flask extention initialization
    bootstrap.init_app(app)

    #addition of forms and views

    return app
