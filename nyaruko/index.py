import os
from flask import Flask
from flask import send_from_directory, render_template
from htmlmin.minify import html_minify
from settings import setting

app = Flask(__name__)

_m = html_minify

''' For favicon ( static/favicon.ico ) '''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host=setting.host, port=setting.port, debug=setting.debug)
