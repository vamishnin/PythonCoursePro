# def multiplier(m=1, source=[1,2,3]):     
#     result = source 
#     for i, x in enumerate(source): 
#         result[i] *= m 
#     return result
def multiplier(m=1, source=[1,2,3]):
    return [m * i for i in source]


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    print(multiplier(5, lst))
    print(multiplier(6, lst))
    print(multiplier(4))
    print(multiplier())