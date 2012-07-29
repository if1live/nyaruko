# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask import send_from_directory, render_template
from flask import session
import config
import auth
from util import *

app = Flask(__name__)


''' For favicon ( static/favicon.ico ) '''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@minify
@auth.requires_auth
def index():
    return render_template('index.html')

@app.route('/login')
@minify
def login():
    return render_template('index.html')


@app.route('/search')
@minify
def search():
    return render_template('main.html')

if __name__ == '__main__':
    app.jinja_env.add_extension('jinja2.ext.i18n')
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
