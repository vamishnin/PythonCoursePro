import socket


def encrypt_words(lst: list, host: str, port: int):
    if not isinstance(lst, list) or not isinstance(host, str) or not isinstance(port, int):
        return None
    res = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for i in lst:
            s.send(i.encode())
            data = s.recv(1024).decode()
            print(f"Sent: {i}, Recieved: {data}")
            res.append(data)
    return res


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9876
    encrypt_words(['qwerty', 'super'], host, port)
    encrypt_words(['version', 'unknown'], host, port)