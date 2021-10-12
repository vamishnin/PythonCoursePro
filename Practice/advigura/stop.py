def is_terminate(word):
    return (word == "Stop" or word == "stop" or word == "STOP")

result = ''
while True:
    user_number = input('enter digit ')
    if is_terminate(user_number):
        break
    if not user_number.isdigit():
        print(f"'{user_number}' is not digit! ")
        continue
    result = result + user_number
    
if len(result) == 0:
    print('Number is empty')
else:
    print(f'Your number is {result}')
