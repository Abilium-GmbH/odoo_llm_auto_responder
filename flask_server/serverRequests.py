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
    print("Server responded with:", response.text)


if __name__ == "__main__":
    ping_server()
    send_data()
