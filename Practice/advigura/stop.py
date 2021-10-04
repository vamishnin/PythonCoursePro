def is_terminate(word):
    return (word == "Stop" or word == "stop" or word == "STOP")

result_str = ''
while True:
    user_number = input('enter digit ')
    if (is_terminate(user_number)):
        break
    if (not user_number.isdigit()):
        print(f"'{user_number}' is not digit! ")
        continue
    result_str=result_str+user_number
    
result = int(result_str) 
print(f'Your number is {result}')
