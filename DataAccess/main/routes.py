from flask import Blueprint, jsonify, request
from Config.config_properties import *
from Models.save_result import SaveResult
from Services.media_service import MediaService

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
@main.route('/index')
def index():
    return jsonify({'message': config.Message})

@main.route('/api/v1/addmedia', methods=["POST"])
def add_media():
    try:
        request_data = request.get_json()
        if not request_data:
            return SaveResult(False, message="request data is not valid").json()
        media_service = MediaService()
        return media_service.add_media(request_data).json()
    except Exception as ex:
        return SaveResult(False, "Exception while processing your request", ex).json()
