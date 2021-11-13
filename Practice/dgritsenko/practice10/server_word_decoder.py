import socket

dictionary = {'name': 'Ivan', 'car': 'sedan', 'work': 'footballer'}
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    while True:
        data, addr = s.recvfrom(1024)
        print('Server got connection from {}'.format(addr))

        print(f'Server got data from client: {data.decode()}')
        try:
            s.sendto(dictionary[data.decode()].encode(), addr)
        except KeyError:
            s.sendto(f'Word "{data.decode()}" can not be decode!'.encode(), addr)
