from multiprocessing.pool import ThreadPool
import requests
import re


def isalive(_link):
    return _link, requests.get(_link).status_code

def main():
    link_re = re.compile(r'(?:url|href|src)=\"(.*?)\"')
    uri = 'https://google.com'

    links = re.findall(link_re, requests.get(uri).text)

    with ThreadPool(len(links)) as p:
        results = p.map(isalive, (link if link.startswith('http') else uri + link for link in links))

    for res in results:
        print(res)

if __name__ == '__main__':
    main()
