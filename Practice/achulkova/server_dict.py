import socket
import pickle


def encrypt(a):
    d = {'aaa': 'one', 'bbb': 'two', 'ccc': 'three'}
    encrypted = []
    for i in a:
        encrypted.append(d[i])
    return encrypted


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    words_lst = pickle.loads(conn.recv(1024))
    conn.send(pickle.dumps(encrypt(words_lst)))
    conn.close()
s.close()