# -*- coding: utf-8 -*-
from urllib import request
import re


req = request.Request('https://google.com')
response = request.urlopen(req)
web_page = response.read().decode('utf-8')

s = re.compile(r'href="(http.*?)"')
res = re.findall(s, web_page)

for link in res:
    req = request.Request(link)
    response = request.urlopen(req)
    status = 'OK' if response.status == 200 else str(response.status)
    print(f'Page: {link} Response: {status}')

