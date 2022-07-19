from flask import Blueprint, request, make_response
import json
from models.account import Account

user_bluepoint = Blueprint('user', __name__, url_prefix='/user')


@user_bluepoint.route('/add', methods=('GET', 'POST'))
def add():
    return "user_add"


@user_bluepoint.route('/get', methods=["GET"])
def get():
    result = Account.query.all()
    print(result[0].name)
    get_args = request.args
    user_name = get_args.get("name") if "name" in get_args else "hello world"
    return "user_name : {0}".format(result[0].name)


@user_bluepoint.route('/post', methods=["POST"])
def post():
    values = request.values
    user_name = values.get("name") if "name" in values else "hello world"
    return "user_name : {0}".format(user_name)


@user_bluepoint.route('/json', methods=["GET"])
def get_json():
    user_info = {"name": "adam"}
    response = make_response(json.dumps(user_info))
    response.headers['Content-Type'] = 'application/json'
    return response
