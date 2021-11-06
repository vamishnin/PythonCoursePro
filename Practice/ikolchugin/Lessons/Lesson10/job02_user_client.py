import socket
import pickle
import time


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Userinfo: {self._name} {self._age}'


class TcpClient:
    def __init__(self, host, port, user):
        self.host = host
        self.port = port
        self._user = user
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(0.1)
        self._socket.send(pickle.dumps(self._user))
        print(f'Sent: {self._user}')
        self._socket.close()


if __name__ == '__main__':
    users = [
        User('Ivanov', 23),
        User('Petrov', 33),
        User('Sidorov', 46)
    ]

    for user in users:
        myclient = TcpClient(host='127.0.0.1', port=9292, user=user)
        myclient.run()