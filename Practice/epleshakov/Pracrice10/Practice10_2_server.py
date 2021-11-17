# Написать клиентское и серверное приложения.
# Клиент при установке соединения отправляет на сервер информацию о пользователе (имя, возраст),
# хранимую в атрибутах объекта класса User.
# Сервер должен выводить информацию о подключенных пользователях.
# Клиентское приложение должно быть запущено несколько раз с различными пользователями
import threading
import socket
import pickle


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        print(f'Connection from address {self._address}')
        data = self._connection.recv(1024)
        u_obj = pickle.loads(data)
        print(f'Current user Name is {u_obj.name} and Age = {u_obj.age}')



class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._runnning = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnning = True
        print('Server is up')
        while self._runnning:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._runnning = False
        self._socket.close()
        print('Server is down')

if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()