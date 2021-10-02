while 1:
    action = input('Input replace action: tab or space ')
    if action.lower() != 'tab' and action.lower() != 'space':
        print('Try again')
    else:
        break

a_str = input('Input text: ')
if action.lower() == 'tab':
    a_str = a_str.replace('\t', ' ' * 4)
else:
    a_str = a_str.replace(' ' * 4, '\t')

print(f'New text: {a_str}')
