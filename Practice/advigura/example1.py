def mymax(*args, **kwargs):
    a = list(args)
    print(f'{max(a)}')
    return max(a)
    
    
mymax(1,2,3,4)
    
def menumerate(lst):
    for i in len(lst):
        print(f'{i} {lst[i]}')
        
        
l = [1, 2, 3, 4, 5]
menumerate(l)