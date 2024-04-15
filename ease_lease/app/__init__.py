from flask import Flask

app = Flask(__name__)
app.secret_key = '123456'

from routes import *
