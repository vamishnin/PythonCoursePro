from multiprocessing.pool import ThreadPool
from urllib import request
from urllib.error import HTTPError
import re


def isalive(_link):
    try:
        response = request.urlopen(_link)
        code = response.status
    except HTTPError as e:
        code = e.code
    return _link, code


def main():
    uri = 'https://google.com'
    link_re = re.compile(r'(?:url|href|src)=\"(.*?)\"')

    links = re.findall(link_re, request.urlopen(uri).read().decode())

    with ThreadPool(len(links)) as p:
        results = p.map(isalive, (link if link.startswith('http') else uri + link for link in links))

    for res in results:
        print(res)


if __name__ == '__main__':
    main()
