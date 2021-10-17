from enum import IntEnum


class Operation(IntEnum):
    WHITESPACES_2_TABS = 1
    TABS_2_WHITESPACES = 2


def space_to_tab(string):
    return string.replace(' '*4, '\t')


def tab_to_space(string):
    return string.replace('\t', ' '*4)


def convert_tabs_whitespaces(path, operation):
    if not isinstance(operation, Operation):
        raise TypeError("operation is not an Operation enum type!")

    data = []
    with open(path, "rt") as f:
        for line in f:
            if operation == Operation.WHITESPACES_2_TABS:
                line = space_to_tab(line)
            else:
                line = tab_to_space(line)
            data.append(line)

    print(repr(data))

    with open(path, "w") as f:
        for line in data:
            f.write(line)


path = 'file.txt'
convert_tabs_whitespaces(path, Operation.WHITESPACES_2_TABS)
convert_tabs_whitespaces(path, Operation.TABS_2_WHITESPACES)
