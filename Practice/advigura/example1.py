def mymax(*args, **kwargs):
    res = args[0]
    for i in args:
        if i > res:
            res = i
            
    print(f'{res}')
    return res
    
    
mymax(1,2,3,4)
    
def menumerate(lst):
    result = []
    for i in range(len(lst)):
        print(f'{i} {lst[i]}')
        result.append([i, lst[i]])
    return result
        
        
l = [1, 2, 3, 4, 5]
menumerate(l)