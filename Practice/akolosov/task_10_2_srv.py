import socket
import pickle
from task_10_2_class import User


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 9876
    s.bind((host, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            user = pickle.loads(conn.recv(1024))
            print(f'User: {user.name} age: {user.age}')
