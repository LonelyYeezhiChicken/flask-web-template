from flask import Flask, request, jsonify
from app import create_app

app = create_app()


@app.route("/api/toTranslate", methods=['POST'])
def toTranslate():
    jsonData = request.get_json()
    inData = jsonData['inData']
    if inData == "hi":
        return jsonify("你好")
    else:
        return jsonify("無法翻譯")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
