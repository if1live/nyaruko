# -*- coding: utf-8 -*-

from functools import wraps
from flask import request, Response, session
from flask import render_template, redirect, url_for
import config

def check_auth(username, password):
  """This function is called to check if a username /
  password combination is valid.
  """
  return username in config.BASIC_AUTH_ID and password == config.BASIC_AUTH_PASSWORD[config.BASIC_AUTH_ID.index(username)]

def authenticate():
  return redirect(url_for('login', redirect=request.path))

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'username' in session:
      return f(*args, **kwargs)
    else:
      return authenticate()
  return decorated
