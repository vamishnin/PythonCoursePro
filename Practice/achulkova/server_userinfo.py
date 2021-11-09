import socket
import pickle
import user

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    print(pickle.loads(conn.recv(1024)))
    conn.close()
s.close()