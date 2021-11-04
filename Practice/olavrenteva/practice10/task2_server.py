import socket
import pickle
from task2_client import User


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 53123
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            user = pickle.loads(conn.recv(1024))
            print(f'User {user} is connected from {addr}')