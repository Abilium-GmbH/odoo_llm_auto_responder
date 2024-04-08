FROM huggingface/transformers-pytorch-gpu:3.3.0
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
EXPOSE 5000
RUN pip install -r requirements.txt

# Set environment variables for Flask
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# Run the Flask application
CMD ["flask", "app.py"]
