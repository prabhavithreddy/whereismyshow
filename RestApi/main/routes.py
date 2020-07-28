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

@main.route('/api/v1/getresults', methods=["GET"])
def get_results(title:str):
    try:
        request_data = request.get_json()
        if not request_data:
            return SaveResult(False, message="request data is not valid").json()
        feed_service = FeedService()
        return feed_service.get_titles(title)
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