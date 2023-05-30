from flask import jsonify, request
from app.api import example_blueprint


@example_blueprint.route('/', methods=['GET'])
def get_examples():
    data = {"message": "Success", "method": "GET"}
    return jsonify(data), 200


@example_blueprint.route('/', methods=['POST'])
def create_example():
    data = {"message": "Success", "method": "POST"}
    return jsonify(data), 201
 
