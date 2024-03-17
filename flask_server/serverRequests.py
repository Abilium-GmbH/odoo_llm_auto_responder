import requests

def ping_server():
    url = "http://127.0.0.1:5000/ping"
    response = requests.get(url)
    if response.status_code == 200:
        print("Server response:", response.text)
    else:
        print("Failed to connect to the server")

if __name__ == "__main__":
    ping_server()
