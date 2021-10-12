def mymax(a, b):
    if a > b:
        return a
    else:
        return b

def printmax(a, b):
    if a > b:
        print(f'print max is {a}')
    else:
        print(f'print max is {b}')
        
var1 = input("Please enter first number ") 
# print (var1)
var2 = input("Please enter second number ") 
print(f'returned max is {mymax(var1,var2)}')
printmax(var1, var2)
