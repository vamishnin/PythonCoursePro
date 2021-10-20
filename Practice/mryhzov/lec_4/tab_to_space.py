# необходимо заменить все символы табуляции на четыре пробела, либо же
# заменить все комбинации из четырех символов пробела на символ табуляции
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


def space_to_tab(s):
    s = s.replace(' '*4, '\t')
    return s


print(tab_to_space(tab_str))
print(space_to_tab(space_str))
