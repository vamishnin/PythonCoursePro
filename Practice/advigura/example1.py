def mymax(*args, **kwargs):
    print(f'{max(args)}')
    return max(args)
    
    
mymax(1,2,3,4)
    
def menumerate(lst):
    result = []
    for i in range(len(lst)):
        print(f'{i} {lst[i]}')
        result.append([i, lst[i]])
    return result
        
        
l = [1, 2, 3, 4, 5]
menumerate(l)