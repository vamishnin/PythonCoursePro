import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    host = '127.0.0.1'
    port = 12345
    data_decode = ['name', 'car', 'world']

    s.connect((host, port))

    for word in data_decode:
        s.sendto(word.encode(), (host, port))

    data_in, addr = s.recvfrom(1024)
    print(f'Decode: {data_in.decode()}')

    while data_in:
        data_in, addr = s.recvfrom(1024)
        print(f'Decode: {data_in.decode()}')
