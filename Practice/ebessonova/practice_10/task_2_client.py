import socket
import random


class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'User: name={self.__name}, age={self.__age}'


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self, data):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(data.encode())
        self._socket.close()


if __name__ == '__main__':
    idx = 0
    while idx < 3:
        user = User(random.choice(['Ivan', 'Fedor', 'Simon', 'Vasiliy', 'Mikhail']), random.randint(20, 30))
        myclient = TcpClient(host='127.0.0.1', port=5555)
        myclient.run(str(user))
        idx += 1
