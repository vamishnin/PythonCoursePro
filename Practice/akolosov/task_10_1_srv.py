import socket

dic = { 'qwerty': 'azerty', 'super': 'duper', 'version': 'latest'}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 9876
    s.bind((host, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                data = data.decode()
                conn.send(dic.get(data, 'There is no word').encode())
