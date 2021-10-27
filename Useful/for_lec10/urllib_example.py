from urllib import request
import re


req = request.Request('https://yandex.ru/pogoda/nizhny-novgorod?lat=56.326887&lon=44.005986')
response = request.urlopen(req)
web_page = response.read().decode()
res = re.findall(r'<span class="temp__value temp__value_with-unit">([+|-]\d)+</span>', web_page)
print(res)
