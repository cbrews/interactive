from app import web, auth, db
from flask import request, abort, jsonify
from user import User

@web.route("/login", methods=["POST"])
def login():
    params = request.get_json()

    if not params or 'username' not in params or 'password' not in params:
        abort(400)

    valid_user = User.getAuthUser(params['username'], params['password'])

    if not valid_user:
        abort(401)

    return valid_user.generateToken(), {'Content-Type': 'text/plain'}

@web.route('/test')
@auth.validate
def test():
    return jsonify(success = True), {'Content-Type': 'application/json'}
