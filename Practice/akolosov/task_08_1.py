def range_uniq(lst: list):
    if not isinstance(lst, list):
        return None
    uniq = set(lst)
    dic = {i: 0 for i in uniq}
    for i in lst:
        dic[i] += 1
    return [k for k, v in sorted(dic.items(), key=lambda item: item[1])]


if __name__ == "__main__":
    a = [4, 7, 2, 4, 7, 4]
    print(f"Uniq range {range_uniq(a)} of {a}")
