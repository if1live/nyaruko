# -*- coding: utf-8 -*-

from functools import wraps
from flask import request, Response
import config

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username in config.BASIC_AUTH_ID and password == config.BASIC_AUTH_PASSWORD[config.BASIC_AUTH_ID.index(username)]

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if config.USE_HTTP_BASIC_AUTH:
            auth = request.authorization
            if not auth or not check_auth(auth.username, auth.password):
                return authenticate()
        return f(*args, **kwargs)
    return decorated
