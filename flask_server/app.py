#this is the flaskserver that runs over docker
import os
from flask import Flask, jsonify, request
from transformers import pipeline
app = Flask(__name__)

# Initialize the pipeline once when the server starts for the llm
qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)


#we define the route /
@app.route('/')
def welcome():
    # return a json
    return jsonify({'status': 'api working'})

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    # Assuming the incoming data is JSON
    data = request.get_json()
    # You can process the data here and then respond
    return jsonify({"message": "Data received", "yourData": data}), 200

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
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
