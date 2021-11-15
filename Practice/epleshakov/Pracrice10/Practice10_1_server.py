# Написать клиентское и серверное приложения.
# Клиент отправляет на сервер список зашифрованных слов, сервер дешифрует слова по словарю
# и возвращает клиенту список расшифрованных слов. Клиент должен вывести полученный список.
import base64
import socket


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        print(f'Подключен клиент {addr=}')
        data = conn.recv(1024)
        if not data: break
        enc_val = data.decode()
        # print(f'{enc_val=}')
        c = decode_key(enc_val, encoded_dict)
        # print(f'{c.decode()=}')
        conn.send(c.decode().encode())
    conn.close()


def decode_key(enc_v: str, enc_dict: dict):
    ret_v = ''
    # print(enc_v)
    if enc_v in enc_dict.values():
        for k, v in enc_dict.items():
            if v == enc_v:
                ret_v = decode_dict[k]
    else:
        ret_v = 'Data not found'
    return ret_v.encode()


def decoder(dict_to_decode: dict):
    decoded_dict = {}
    for key, val in dict_to_decode.items():
        dec = []
        enc = base64.urlsafe_b64decode(val).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        v = (key, "".join(dec))
        decoded_dict.update([v])
    return decoded_dict


def encoder(dict_to_encode: dict):
    l = {}
    for key, val in dict_to_encode.items():
        enc = []
        for i in range(len(val)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(val[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        v = (key, base64.urlsafe_b64encode("".join(enc).encode()).decode())
        l.update([v])
    return l


decode_dict = {'odin': '111', 'dva': '222', 'tri': '333', 'chetyre': '4445445'}
encoded_dict = encoder(decode_dict)
start_server()
