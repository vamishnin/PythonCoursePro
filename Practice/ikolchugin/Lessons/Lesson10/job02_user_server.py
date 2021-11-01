import threading
import socket
import pickle
from job02_user_client import User


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr
        self._user = None

    def run(self):
        print(f'Connection from address {self._address}')
        self._user = pickle.loads(self._connection.recv(1024))
        print(f'Received data {self._user}')
        self._connection.close()
        print(f'Closed connection from {self._address}')


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print('Server is up')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=9292)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()

