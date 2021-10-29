import threading
import socket
import pickle

class ClientThread(threading.Thread):
    def __init__(self, conn, addr, crypto_dict):
        super().__init__()
        self._connection = conn
        self._address = addr
        self._crypto_dict = crypto_dict
        self._encrypted = None
        self._decrypted = None

    def run(self):
        print(f'Connection from address {self._address}')
        self._encrypted = pickle.loads(self._connection.recv(1024))
        print(f'Received encrypted {self._encrypted}')
        self._decrypted = [self._crypto_dict.get(w, None) for w in self._encrypted]
        self._connection.send(pickle.dumps(self._decrypted))
        print(f'Sent decrypted {self._decrypted}')
        self._connection.close()
        print(f'Closed connection from {self._address}')


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False
        self._crypto_dict = self.__generate_crypto()

    @staticmethod
    def __generate_crypto():
        return {f'word{i}': f'WORD{i}' for i in range(20)}

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print('Server is up')
        print(f'{self._crypto_dict=}')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr, self._crypto_dict).start()

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

