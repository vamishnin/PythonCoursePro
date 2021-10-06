def format_str(string: str, dic: dict):
    '''
    The function replaces the keys of dictionary dict by the values in the string
    '''
    for key in dic:
        if key in string:
            string = string.replace(key, dic[key])
    return string


if __name__ == "__main__":
    string = "qwerty"
    print(format_str(string, {'qw': 'az'}))

    string = 'Brave New World'
    dic = {'Brave': 'О дивный', 'New': 'новый', 'World': 'мир'}
    print(format_str(string, dic))
