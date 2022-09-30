
from flask import Blueprint, jsonify, request
from app.service.translateService import TranslateService

apiController = Blueprint('apiController', __name__)


@apiController.route("/toTranslate", methods=['POST'])
def toTranslate():
    jsonData = request.get_json()
    inData = jsonData['inData']
    return TranslateService.getTranslate(inData)
