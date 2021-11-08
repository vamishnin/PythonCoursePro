import argparse
import socket
import pickle
from task_10_2_class import User


def server_connect(user, host: str, port: int):
    if not isinstance(user, User) or not isinstance(host, str) or not isinstance(port, int):
        return None
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(pickle.dumps(user))


def parse_args():
    parser = argparse.ArgumentParser(description='Connect to server.')
    parser.add_argument('-s', '--server', type=str, default='127.0.0.1', help="servername/IP")
    parser.add_argument('-p', '--port', type=int, default=9876, help="port")
    parser.add_argument('name', help="Username")
    parser.add_argument('age', help="user's age")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    server_connect(User(args.name, args.age), args.server, args.port)
