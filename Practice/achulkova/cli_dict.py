import socket
import pickle

words = ['aaa', 'bbb', 'ccc']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
s.send(pickle.dumps(words))
print(pickle.loads(s.recv(1024)))
s.close()

