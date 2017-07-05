from flask import render_template
from iter import app
from .utils import get_sites


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sites=get_sites())
