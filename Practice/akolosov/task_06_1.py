# a generator has to have the stop condition for useing in list comprehension
def chargen(num: int):
    i = 0
    while i < num:
        for c in '0123456789':
            yield c
            i += 1
            if i >= num:
                break


if __name__ == "__main__":
    words = [c + c for c in chargen(10)]
    print(words)
