# initial implementation changed list passed as argument

def multiplier(m=1, source=(1,2,3)):
    return [m * i for i in source]


lst = [1, 0, -5, 100]
print(multiplier(3, lst))
print(multiplier(3, lst))
print(multiplier())
