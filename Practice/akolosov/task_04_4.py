def tab_spaces(in_data, mode=0):
    '''
    mode:
    0 - replace tab by 4 spaces
    1 - replace 4 spaces by tab
    '''
    if isinstance(in_data, str):
        if mode == 0:
            # set tab position in 4 and tab expands to 1-4 spaces in dependency on position
            return in_data.expandtabs(4)
            # tab expands to exactly 4 spaces
            # return in_data.replace('\t', ' ' * 4)
        else:
            return in_data.replace(' ' * 4, '\t')
    # else - to be continue


s = "12345\t6789\t0123"
print(tuple(s))
s = tab_spaces(s)
print(tuple(s))
s = tab_spaces(s, 1)
print(tuple(s))
