import os


def tab_spaces_str(in_data, mode=0):
    '''
    Replace tab <=> spaces in a string
    mode:
    0 - replace tab by 4 spaces
    1 - replace 4 spaces by tab
    '''
    if isinstance(in_data, str):
        if mode == 0:
            # set tab position in 4 and tab expands to 1-4 spaces
            # in dependency on position
            return in_data.expandtabs(4)
            # tab expands to exactly 4 spaces
            # return in_data.replace('\t', ' ' * 4)
        else:
            return in_data.replace(' ' * 4, '\t')
    else:
        return None


def tab_spaces_file(in_data, mode=0):
    '''
    Replace tab <=> spaces in a file
    mode:
    0 - replace tab by 4 spaces
    1 - replace 4 spaces by tab
    '''
    if isinstance(in_data, str):
        with open(in_data) as reader, \
             open(in_data + '.tmp', 'w') as writer:
            for s in reader:
                s = tab_spaces_str(s, mode)
                if s != None:
                    writer.write(s)

        os.remove(in_data)
        os.rename(in_data + '.tmp', in_data)
    return None


def print_file(f):
    '''
    Print content of the file
    '''
    print(f"File: {f}")
    with open(f) as reader:
        for s in reader:
            print(repr(s))
    return None


if __name__ == "__main__":
    s = "12345\t6789\t0123"
    print(repr(s))
    s = tab_spaces_str(s)
    print(repr(s))
    s = tab_spaces_str(s, 1)
    print(repr(s))

    f = "Practice/akolosov/test.txt"
    print_file(f)
    tab_spaces_file(f, 1)
    print_file(f)
    tab_spaces_file(f, 0)
    print_file(f)
