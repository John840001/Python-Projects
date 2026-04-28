import requests

# 1. GET request with query parameters
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# Parse JSON response
data = response.json()
print(data)

# Check status code
print(f"Status Code: {response.status_code}")

# 2. POST request with JSON data
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)

# Parse JSON response
data = response.json()
print(data)

# Check status code
print(f"Status Code: {response.status_code}")
