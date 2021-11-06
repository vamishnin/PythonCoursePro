import re
from urllib import request
from urllib.error import URLError

req = request.Request('http://google.com')
response = request.urlopen(req)
web_page = response.read()
links = re.findall('https?://[^"]+', str(web_page))
for link in links:
    req_link = request.Request(link)
    try:
        response_code = request.urlopen(req_link).getcode()
        if response_code == 200 or response_code == 302:
            print(f'{link} is valid')
        else:
            print(f'{link} is not valid')
    except URLError:
        print(f'{link} - Connection error has happened on attempt to get the link')
