# this is the flaskserver that runs over docker
import os
from flask import Flask, jsonify, request
from transformers import pipeline
from flask_executor import Executor
from flask_sqlalchemy import SQLAlchemy
import logging
import requests

app = Flask(__name__)
executor = Executor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///llm_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

# Initialize the pipeline once when the server starts for the llm
qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)

# Create the db Class (items that will be stored in the db)
class LLMRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<LLMRequest {self.id}>'

# create the db when the server is created
with app.app_context():
    db.create_all()

#function to store data in the db
@app.route('/store', methods=['POST'])
def store_data():
    try:
        data = request.get_json()
        context = data.get('context')
        if not context:
            return jsonify({'error': 'please provide context'}), 400
        new_request = LLMRequest(context=context)
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'context stored'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to store data', 'exception': str(e)}), 500


#function to load all data from the db
@app.route('/load', methods=['GET'])
def load_data():
    try:
        requests = LLMRequest.query.all()
        result = [{'id': req.id, 'context': req.context} for req in requests]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Failed to load data', 'exception': str(e)}), 500


@app.route('/reset', methods=['GET'])
def reset_database():
    try:
        # Delete all records from LLMRequest
        num_rows_deleted = db.session.query(LLMRequest).delete()
        db.session.commit()
        return jsonify({'message': f'Successfully deleted {num_rows_deleted} records.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to reset database', 'exception': str(e)}), 500


# we define the route /
@app.route('/')
def welcome():
    # return a json
    return jsonify({'status': 'api working'})


@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    # Assuming the incoming data is JSON
    data = request.get_json()
    executor.submit(llm_answer, data)
    # You can process the data here and then respond
    return 'LLM started', 202


def llm_answer(data):
    llm_requests = LLMRequest.query.all()
    context = "\n".join(req.context for req in llm_requests)
    question = data.get("question")
    qId = data.get("qId")
    if not context or not question:
        return logger.info("Please provide both a context and a question"), 400

    answer = qa_pipeline(context=context, question=question)
    str_ans = answer.get("answer")
    llm_return = {"params":{'id': qId, 'ai_answer': str_ans}}
    logger.info(f"LLM return: {str_ans}")
    try:
        response = requests.post("http://web:8069/ai_answer/answer", json=llm_return)
        logger.info(f"Response from AIAnswerController: {response.text}")
    except Exception as e:
        logger.error(f"Failed to send data to AIAnswerController: {str(e)}")
        return jsonify({'error': 'Failed to communicate with AIAnswerController', 'exception': str(e)}), 500

    return logger.info(f"Answer: {answer}, Question ID: {qId}"), 200


if __name__ == '__main__':
    # define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
