import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Test Title",
    "body": "Test Body",
    "userId": 1
}

response = requests.post(url, json=data)

assert response.status_code == 201
