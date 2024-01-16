import requests

# Making an HTTP GET request
response = requests.get("https://www.example.com")

# Printing the status code and content
print("Status Code:", response.status_code)
print("Content:")
print(response.text)
