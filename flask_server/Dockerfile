FROM huggingface/transformers-pytorch-gpu:3.3.0
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
EXPOSE 5000
RUN pip install -r requirements.txt

# Set environment variables for Flask
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Optionally, you can specify a port with FLASK_RUN_PORT
# ENV FLASK_RUN_PORT=5000

# Run the Flask application
CMD ["flask", "run"]
