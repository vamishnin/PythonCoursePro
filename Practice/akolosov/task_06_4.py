import itertools


def three_in_one(*args):
    if len(args) == 3 and isinstance(args[0], list) and isinstance(args[1], list) and isinstance(args[2], list):
        return [i for i in itertools.chain(args[0], args[1], args[2])]
    else:
        return None


def five_and_more(lst: list):
    if isinstance(lst, list):
        return [i for i in itertools.filterfalse(lambda x: len(x) < 5, lst)]
    else:
        return None


def many_from_one(s: str):
    if isinstance(s, str):
        return [tuple(i) for i in itertools.combinations(s, 4)]
    else:
        return None


if __name__ == "__main__":
    print(three_in_one([1, 2, 3], [4, 5], [6, 7]))
    print(three_in_one([1, 2, 3], [4, 5], 6))
    print(three_in_one([1, 2, 3]))

    print(five_and_more(['hello', 'i', 'write', 'cool', 'code']))
    print(five_and_more('hello'))

    print(many_from_one("password"))
