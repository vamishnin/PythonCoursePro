import socket
import pickle


class User:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def __str__(self):
        return f'{self._name} {self._surname}'


if __name__ == '__main__':
    # user = User('Ivan', 'Ivanov')
    # user = User('Petr', 'Petrov')
    user = User('Sidr', 'Sidorov')

    with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        host = '127.0.0.1'
        port = 53123
        s.connect((host, port))
        s.send(pickle.dumps(user))
