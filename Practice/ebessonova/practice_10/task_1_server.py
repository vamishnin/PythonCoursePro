# -*- coding: utf-8 -*-
import socket


word_dict = {'word': 'слово', 'letter': 'буква', 'sentence': 'предложение'}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
while True:
    elem, addr = s.recvfrom(1024)
    print('Server got data from client: {}'.format(elem.decode()))
    s.sendto((word_dict[elem.decode()].encode() if word_dict[elem.decode()] else 'not in dict'.encode()), addr)
s.close()
