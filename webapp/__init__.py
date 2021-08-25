from flask import Flask
from config import config_options

def create_app(config_name):
    app = flask(__name__)
    app.config.from_object(config_options[config_name])
 
    #registering the blueprint
    from webapp.auth import auth as blue_print
    app.register_blueprint(blue_print)
    
    #registering the blueprint
    from webapp.main import main as blue_print
    app.register_blueprint(blue_print)

    #Setting up configuration
    from .request import configure_request
    configure_request(app)


    return app