from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

from main.routes import main

app.register_blueprint(main)