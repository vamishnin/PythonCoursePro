import socket
import pickle


dict = {"а": "ю", "б": "я", "в": "а", "г": "б", "д": "в", "е": "г", "ё": "д", "ж": "е", "з": "ё",
        "и": "ж", "й": "з", "к": "и", "л": "й", "м": "к", "н": "л", "о": "м", "п": "н", "р": "о",
        "с": "п", "т": "р", "у": "с", "ф": "т", "х": "у", "ц": "ф", "ч": "х", "ш": "ц", "щ": "ч",
        "ъ": "ш", "ы": "щ", "ь": "ъ", "э": "ы", "ю": "ь", "я": "э"}

with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    host = '127.0.0.1'
    port = 53123
    s.bind((host, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            got_list = (pickle.loads(conn.recv(4096)))

            list_to_send = []
            for word in got_list:
                decoded_word = ''
                for letter in word:
                    decoded_word += dict.get(letter.lower(), letter)
                list_to_send.append(decoded_word)

            conn.send(pickle.dumps(list_to_send))

