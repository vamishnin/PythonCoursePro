import socket
import pickle


with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    host = '127.0.0.1'
    port = 53123
    s.connect((host, port))

    list_to_send = ["Мхёв", "мвфкфуб", "окт"]
    s.send(pickle.dumps(list_to_send))

    got_list = (pickle.loads(s.recv(4096)))
    print(got_list)

