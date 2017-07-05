from flask import render_template, send_from_directory

from iter import app, static_dir

from .utils import get_sites


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(static_dir,
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sites=get_sites())
