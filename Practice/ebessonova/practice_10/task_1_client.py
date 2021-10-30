# -*- coding: utf-8 -*-
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
lst = ['letter', 'sentence', 'word', 'paragraph']
for el in lst:
    s.sendto(el.encode(), (host, port))
data, addr = s.recvfrom(1024)
print(f'Перевод: {data.decode()}')
while data:
    data, addr = s.recvfrom(1024)
    print(f'Перевод: {data.decode()}')
s.close()
