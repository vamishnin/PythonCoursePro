def ispalindrome(a: str, b=0):
    '''
    Check mode(second argument):
    0 - check a word
    1 - check a sentence
    Retuns:
    1 - input word is a palindrome
    0 - input word isn't a palindrome
    -1 - input isn't correct
    '''
    if b == 1:
        a = a.replace(' ','')
    
    if a.isalpha():
        res = 1
        for i in range(0,len(a)//2):
            if a[i] != a[-1-i]:
                res = 0
                break
    else:
        res = -1
    return res


str = 'reviver'
print(f'Input: {str=}, result: {ispalindrome(str)}')

str = 'qwerty'
print(f'Input: {str=}, result: {ispalindrome(str)}')

str = 'а роза упала на лапу азора'
mode = 1
print(f'Input: {str=}, result: {ispalindrome(str)}')
print(f'Input: {str=} & {mode=}, result: {ispalindrome(str, mode)}')
