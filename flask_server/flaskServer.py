# this file runs a test-flaskserver
from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import pipeline

from llm_integration import get_llm_response

app = Flask(__name__)
CORS(app)

# Initialize the pipeline once when the server starts for the llm
qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/data', methods=['GET', 'POST'])
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

# /llm command
@app.route('/llm', methods=['POST'])
def llm_endpoint():
    data = request.get_json()
    context = data.get("context")
    question = data.get("question")

    if not context or not question:
        return jsonify({"error": "Please provide both a context and a question"}), 400

    answer = qa_pipeline(context=context, question=question)
    return jsonify(answer), 200


if __name__ == '__main__':
    app.run(debug=True)
