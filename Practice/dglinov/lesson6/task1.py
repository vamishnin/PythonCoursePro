'''
В чем ошибка в данной программе и как ее можно исправить?
'''

def chargen(): 
#    while True: 
        for c in '0123456789': 
            yield c
 
words = [c + c for c in chargen()][:10] 
print(words)