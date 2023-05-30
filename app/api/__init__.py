from flask import Blueprint

example_blueprint= Blueprint('example', __name__, url_prefix='/example')

from app.api.routes import routes