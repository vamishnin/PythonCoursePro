# -*- coding: utf-8 -*-
import socket


word_dict = {'word': 'слово', 'letter': 'буква', 'sentence': 'предложение'}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
while True:
    elem, addr = s.recvfrom(1024)
    print(f'Server got data from client: {elem.decode()}')
    try:
        s.sendto(word_dict[elem.decode()].encode(), addr)
    except KeyError:
        s.sendto(f'Слово "{elem.decode()}" не найдено в словаре'.encode(), addr)
s.close()
