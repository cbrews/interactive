import flask
from app import web, db

# TODO: Really clean this up to be just a single function please :D
#
def http_error(code, description="An error occurred."):
    return flask.jsonify({'error': description}), code

@web.errorhandler(404)
def no_route(e):
    return http_error(404, "This route could not be found.")

@web.errorhandler(403)
def no_auth(e):
    return http_error(403, "Unauthorized.")

@web.errorhandler(405)
def no_auth(e):
    return http_error(405, "Method not allowed.")

@web.errorhandler(503)
def server_error(e):
    return http_error(503)
