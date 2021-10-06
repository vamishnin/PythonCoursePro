def format_str(string: str, dic: dict):
    '''
    The function replaces the keys of dictionary dict by the values in the string
    '''
    for key in dic:
        if key in string:
            string = string.replace(key,dic[key])
    return string


if __name__ == "__main__":
    str = "qwerty"
    print(format_str(str, {'qw': 'az'}))

    str = 'Brave New World'
    dict = {'Brave': 'О дивный', 'New': 'новый', 'World': 'мир'}
    print(format_str(str, dict))
