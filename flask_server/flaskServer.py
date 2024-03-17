from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    # You can return a simple string
    # return "pong"

    # Or, for a more API-like response, return a JSON
    return jsonify({"message": "pong"}), 200
