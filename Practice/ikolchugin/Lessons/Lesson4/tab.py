def space_to_tab(string):
    return string.replace(' '*4, '\t')


def tab_to_space(string):
    return string.replace('\t', ' ' * 4)


str_to_tab = """
    This is strings
    with 4 spaces    and more 4 spaces
"""


str_to_spaces = """
	This is string
	with 1 tabs     and more tabs
"""

print(space_to_tab(str_to_tab))
print(tab_to_space(str_to_spaces))
