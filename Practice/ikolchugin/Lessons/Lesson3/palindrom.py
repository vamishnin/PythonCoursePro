#
# def is_palindrom(input_string):
#     t = input_string if isinstance(input_string, str) \
#         else str(input_string)
#     return t == t[::-1]

def is_palindrom(input_string):
    return input_string == input_string[::-1] if isinstance(input_string, str)\
        else False

test_array=[
    123,
    12321,
    '12321',
    'АБВБА'
]

for v in test_array:
    print(f'{v} is palindrom: {is_palindrom(v)}')
