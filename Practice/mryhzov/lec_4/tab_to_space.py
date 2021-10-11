tab_str = """
    Привет, как дела?
        Как поживаешь \t?
    """
space_str = """
    Здорова,    нормально.
    Как сам?    
    """


def tab_to_space(s):
    s = s.replace('\t', ' '*4)
    return s


def space_to_tab(t):
    t = t.replace(' '*4, '\t')
    return t


print(tab_to_space(tab_str))
print(space_to_tab(space_str))
