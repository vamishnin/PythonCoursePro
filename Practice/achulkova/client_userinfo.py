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
    a = user.User('Petr', '25')
    b = user.User('Fedor', '40')
    c = user.User('Ivan', '18')
    myClient1 = TcpClient(host='127.0.0.1', port=12345, users=a)
    myClient2 = TcpClient(host='127.0.0.1', port=12345, users=b)
    myClient3 = TcpClient(host='127.0.0.1', port=12345, users=c)
    myClient1.run()
    myClient2.run()
    myClient3.run()
