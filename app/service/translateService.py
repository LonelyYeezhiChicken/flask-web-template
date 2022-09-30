from flask import jsonify
from app.repository.translateRepository import TranslateRepository


class TranslateService:

    def getTranslate(inData):
        if inData != "":
            outData = TranslateRepository.translate_content_ch(inData)
            return jsonify(outData)
        else:
            return jsonify("無法翻譯")
