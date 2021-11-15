import socket
import pickle


def decrypt(a):
    d = {'aaa': 'one', 'bbb': 'two', 'ccc': 'three'}
    decrypted = []
    for i in a:
        if not d.get(i):
            print(f'Key {i} not found in the dictionary')
            break
        decrypted.append(d[i])
    return decrypted


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12348
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    words_lst = pickle.loads(conn.recv(1024))
    conn.send(pickle.dumps(decrypt(words_lst)))
    conn.close()
s.close()