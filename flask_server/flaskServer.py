#this file runs a test-flaskserver
from flask import Flask,jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/data', methods=['GET','POST'])
def receive_data():
    # Assuming the incoming data is JSON
    data = request.get_json()
    # You can process the data here and then respond
    return jsonify({"message": "Data received", "yourData": data}), 200


@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    # You can return a simple string
    # return "pong"

    # Or, for a more API-like response, return a JSON
    return jsonify({"message": "pong"}), 200
