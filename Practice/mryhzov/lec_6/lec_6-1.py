def chargen():    # кастомный генератор
    for c in '0123456789':
        yield c


for c in chargen():
    words = [c + c for c in chargen()][:10]    # списковое выражение
print(words)

