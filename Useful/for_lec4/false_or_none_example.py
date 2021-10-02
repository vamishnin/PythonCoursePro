def greater(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a > b
    return None


a = 10
b = "qqqq"
res = greater(a, b)
if res is True:
    print(f"{a} is greater")
elif res is False:
    print(f"{b} is greater")
else:
    print('Incorrect values')
