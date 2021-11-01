import string
import pickle
from random import shuffle


def encrypt(_s, _crypto_dict):
    return ''.join([_crypto_dict.get(x, x) for x in _s ])


def crypto_dict():
    cyr_letters = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    symbols = [s for s in set(string.digits+string.ascii_letters + cyr_letters + cyr_letters.upper())]
    shuffled_symbols = symbols.copy()
    shuffle(shuffled_symbols)
    return dict(zip(symbols, shuffled_symbols))


def rev_crypto_dict(_crypto_dict):
    return {v: k for k, v in _crypto_dict.items()}


def decrypt(_s, _crypto_dict):
    return encrypt(_s, _crypto_dict)


if __name__ == '__main__':
    __src_string = 'test string'

    secret_dict = crypto_dict()
    rev_secret_dict = rev_crypto_dict(secret_dict)

    print(secret_dict)
    with open('crypt_dict.bin', 'wb') as f:
        pickle.dump(secret_dict, f)
    with open('decrypt_dict.bin', 'wb') as f:
        pickle.dump(rev_secret_dict, f)

    rev_secret_dict = rev_crypto_dict(secret_dict)
    print(rev_secret_dict)

    __encrypted_string = encrypt(__src_string, secret_dict)
    print(__encrypted_string)

    __decrypted_string = decrypt(__encrypted_string, rev_secret_dict)
    print(__decrypted_string)

    encrypted_words = [
        encrypt(f'word{i}', secret_dict) for i in range(30)
    ]
    print(encrypted_words)
