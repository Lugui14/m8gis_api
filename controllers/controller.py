from flask import Blueprint

route = Blueprint('route', __name__)

@route.route("/")
def teste():
    return 'hello world!'