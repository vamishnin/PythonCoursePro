def large_num(num1, num2):
    m = int(num1)
    n = int(num2)
    if type(m) and type(n) is int:
        if m > n:
            print(m)
        else:
            print(n)
    else:
        print("arguments is not numeric")
        # на самом деле не дойдет до этого, но обойти это, используя
        # кроме как try/except, я без гугла не додумался


print('Input two some numeric')
a = input('1-st numeric: ')
b = input('2-nd numeric: ')
large_num(a, b)
