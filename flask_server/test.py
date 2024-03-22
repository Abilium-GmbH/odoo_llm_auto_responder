# This file is for tests on the LLM
from transformers import pipeline


# Function to read contexts from a text file
def read_data_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data

# Path to the text file containing contexts
file_path_context = "C:/UniBe/Informatik/PSE/context.txt"
contexts = read_data_from_file(file_path_context)

#Path to the text file containing questions
file_path_questions = "C:/UniBe/Informatik/PSE/questions.txt"
questions = read_data_from_file(file_path_questions)


qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)

# Iterate over each context and question
for question in questions:
    print("Question:", question)
    for context in contexts:
        answer = qa_pipeline(context=context, question=question)
        print("Answer:", answer['answer'])
        print("Score:", answer['score'])
        print("Start:", answer['start'])
        print("End:", answer['end'])
        print()
        break  # Break out of the inner loop after obtaining the first answer
    print()