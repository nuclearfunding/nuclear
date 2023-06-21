from flask import Blueprint
import json

organization_api = Blueprint('organization', __name__, url_prefix='/organization')


@user_api.route('/create', methods=['POST'])
def create_organization():
    return json.dumps({'organization': 'created'}), 200


@user_api.route('/update', methods=['POST'])
def update_organization():
    return json.dumps({'organization': 'updated'}), 200


@user_api.route('/delete', methods=['POST'])
def delete_organization():
    return json.dumps({'organization': 'deleted'}), 200


@user_api.route('/get', methods=['GET'])
def get_organization():
    return json.dumps({'organization': 'get'}), 200
