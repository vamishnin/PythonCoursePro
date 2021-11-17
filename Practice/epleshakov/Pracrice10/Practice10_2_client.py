# Написать клиентское и серверное приложения.
# Клиент при установке соединения отправляет на сервер информацию о пользователе (имя, возраст),
# хранимую в атрибутах объекта класса User.
# Сервер должен выводить информацию о подключенных пользователях.
# Клиентское приложение должно быть запущено несколько раз с различными пользователями
#  py -3.10 .\Practice10_2_client.py
import socket
import random
import pickle


class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        while True:
            self._socket.send(user_to_bytes(user))


class User:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, value):
        self._name = value

    @name.getter
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        self._name = None

    @age.setter
    def age(self, value):
        self._age = value

    @age.getter
    def age(self):
        return self._age

    @age.deleter
    def age(self):
        self._age = None

def user_to_bytes(user: User):
    return pickle.dumps(user, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    name = 'Python client ' + str(random.randint(1, 1000))
    myclient = TcpClient(host='127.0.0.1', port=5555, name=name)
    n_name = input('Имя пользователя: ')
    n_age = input('Возраст пользователя: ')
    user = User(n_name, n_age)
    myclient.run()

