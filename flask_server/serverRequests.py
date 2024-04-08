# this file pings the server and fetches the response
import requests

def ping_server():
    url = "http://127.0.0.1:5000/ping"
    response = requests.get(url)
    if response.status_code == 200:
        print("Server response:", response.text)
    else:
        print("Failed to connect to the server")

def send_data():
    url = 'http://localhost:5000/data'
    data = {'key': 'value', 'number': 123}
    response = requests.post(url, json=data)
    print("Response status code:", response.status_code)
    print("Server responded with:", response.text)

#curl -X POST -H "Content-Type: application/json" \-d "{\"context\":\"Here is some context about the question.\", \"question\":\"What is the question?\"}" \http://localhost:5000/llm

if __name__ == "__main__":
    send_data()
