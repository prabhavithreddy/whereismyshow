from flask import Blueprint, jsonify, request
from config.config_properties import *
from models.save_result import SaveResult
from services.feed_service import FeedService
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
@main.route('/index')
def index():
    return jsonify({'message': config.Message})


feed_service = FeedService()
@main.route('/api/v1/getresults', methods=["GET"])
def get_results():
    try:
        title = request.args["title"]
        if not title:
            return SaveResult(False, message="Title is required").json()
        return jsonify(feed_service.get_titles(title))
    except Exception as ex:
        return SaveResult(False, "Exception while processing your request", ex).json()

@main.route('/api/v1/getresultstest', methods=["GET"])
def get_results_test():
    try:
        title = request.args["title"]
        if not title:
            return SaveResult(False, message="Title is required").json()
        feed_service = FeedService()
        return jsonify(feed_service.get_titles_test(title))
    except Exception as ex:
        return SaveResult(False, "Exception while processing your request", ex).json()

@main.route('/api/v1/getproviders', methods=["GET"])
def get_providers():
    try:
        return jsonify(feed_service.get_providers())
    except Exception as ex:
        return SaveResult(False, "Exception while processing your request", ex).json()