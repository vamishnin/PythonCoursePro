def return_max(a: int, b: int):
    if a > b:
        res = a
    else:
        res = b
    return res


a = 9
b = 11
print(f"Max of {a=} and {b=} is {return_max(a ,b)}")
