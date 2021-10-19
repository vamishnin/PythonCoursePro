def multiplier(m=1, source=[1,2,3]):      
    # result = source.copy()
    result = []
    for i, x in enumerate(source): 
        result.append(source[i] * m)
    return result

src = [1,2,3]
 
print(f"{multiplier(5, src)}") 
print(f"{multiplier(5, src)}") 
# [5, 10, 15] 
print(f"{multiplier(12, [1,2])}") 
# [12, 24] 
