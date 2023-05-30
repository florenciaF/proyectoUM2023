from flask import Flask
from config import Config

def create_app(config_object='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from app.api import example_blueprint
    app.register_blueprint(example_blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return {'message': 'Not Found'}, 404

    return app