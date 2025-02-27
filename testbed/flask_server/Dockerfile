FROM python:3.10
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip3 install -r requirements.txt

# Set environment variables for Flask
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Optionally, you can specify a port with FLASK_RUN_PORT
# ENV FLASK_RUN_PORT=5000

# Start the Flask application when the container launches
EXPOSE 5001
CMD ["python3", "-m", "flask", "run"]
