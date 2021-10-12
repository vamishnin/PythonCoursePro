def is_terminate(word):
    return (word == "Stop" or word == "stop" or word == "STOP")

# result = ''
myarray = []
while True:
    user_number = input('Enter digit for array. Enter "stop" to finish ')
    if is_terminate(user_number):
        break
    if not user_number.isdigit():
        print(f"'{user_number}' is not digit! ")
        continue
    myarray.append(int(user_number))
    
    
print(f'Your array is {myarray}')

i = 0
while i < len(myarray) - 1:
    min_ind = i
    j = i + 1
    while j < len(myarray):
        if myarray[j] < myarray[min_ind]:
            min_ind = j
        j += 1
    myarray[i], myarray[min_ind] = myarray[min_ind], myarray[i]
    i += 1
    
print(f'Sorteed array {myarray}')