from flask import Flask, render_template
import os
from .utils import get_sites

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

static_dir = os.path.abspath(os.path.join(app.root_path,
                                          os.pardir,
                                          'static'))

from . import api
