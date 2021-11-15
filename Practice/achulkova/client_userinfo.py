import socket
import pickle
import user
import time


class TcpClient:
    def __init__(self, host, port, users):
        self.host = host
        self.port = port
        self.users = users
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(3)
        self._socket.send(pickle.dumps(self.users))
        self._socket.close()


if __name__ == '__main__':
    my_clients = []
    for each in (('Petr', '25'), ('Fedor', '40'), ('Ivan', '18')):
        my_clients.append(TcpClient(host='127.0.0.1', port=12346, users=user.User(*each)))
    for my_client in my_clients:
        my_client.run()
