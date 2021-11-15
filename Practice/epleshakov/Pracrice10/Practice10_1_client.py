# Написать клиентское и серверное приложения.
# Клиент отправляет на сервер список зашифрованных слов, сервер дешифрует слова по словарю
# и возвращает клиенту список расшифрованных слов. Клиент должен вывести полученный список.
import socket


encoded_list = ['wqDClcKa', 'wpbCqMKT', 'wqfCpcKc', 'wpfCnMKZwqnCrcKmwpo=', 'bhefuweuwue']


def start_client(list_to_send: list):
    wrds = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    for val in list_to_send:
        s.send(val.encode())
        d = s.recv(1024)
        wrds.append(d.decode())
    s.close()
    return wrds


print(start_client(encoded_list))
