# Написать функцию count_symbol: считает сколько раз символ встречается в строке.
def count_symbol(txt, symb):
    n = 0
    for sym in txt:
        if sym == symb:
            n += 1
    return n

print (count_symbol("Hi, Elvis, I am here!", "i"))