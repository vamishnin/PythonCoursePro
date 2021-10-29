
def encrypt(_s, _key):
    return '.'.join([str(ord(x) ^ _key) for x in _s])


def decrypt(_s, _key):
    return ''.join([chr(int(i) ^ _key) for i in _s.split('.')])


if __name__ == '__main__':
    __src_string = 'test string'
    __key = 1234

    __encrypted_string = encrypt(__src_string, __key)
    print(__encrypted_string)

    __decrypted_string = decrypt(__encrypted_string, __key)
    print(__decrypted_string)
