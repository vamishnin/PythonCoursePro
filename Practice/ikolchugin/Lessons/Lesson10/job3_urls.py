from multiprocessing.pool import ThreadPool
import urllib
import re


def isalive(_link):
    a=urllib.urlopen(_link)
    return _link,a.g

def main():
    uri = 'https://google.com'
    a = urllib.urlopen(uri)

def main1():
    link_re = re.compile(r'(?:url|href|src)=\"(.*?)\"')
    uri = 'https://google.com'

    links = re.findall(link_re, request.urlopen(uri).read().decode())

    print(links)
    with ThreadPool(len(links)) as p:
        results = p.map(isalive, (link if link.startswith('http') else uri + link for link in links))

    for res in results:
        print(res)

if __name__ == '__main__':
    main()
