from flask import Blueprint
import json

user_api = Blueprint('user', __name__, url_prefix='/user')


@user_api.route('/create', methods=['POST'])
def create_user():
    return json.dumps({'user': 'created'}), 200