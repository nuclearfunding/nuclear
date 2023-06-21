from flask import Blueprint
import json

user_api = Blueprint('user', __name__, url_prefix='/user')


@user_api.route('/create', methods=['POST'])
def create_user():
    return json.dumps({'user': 'created'}), 200


@user_api.route('/update', methods=['POST'])
def update_user():
    return json.dumps({'user': 'updated'}), 200


@user_api.route('/delete', methods=['POST'])
def delete_user():
    return json.dumps({'user': 'deleted'}), 200


@user_api.route('/get', methods=['GET'])
def get_user():
    return json.dumps({'user': 'get'}), 200
