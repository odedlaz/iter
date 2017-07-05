from flask import Flask, render_template
from .utils import get_sites

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

from . import api
