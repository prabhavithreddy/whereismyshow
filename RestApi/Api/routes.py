from flask import Flask, jsonify
from flask_restful import Api
from utils.logger import Logger

app = Flask(__name__)
api = Api(app)

logger = Logger(__name__)

@app.route('/api/v1/welcome', methods=["GET"])
def welcome():
    logger.info("welcome")
    return jsonify({'message': app.config['WELCOME']})