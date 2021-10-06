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
        for i in range(len(a)//2):
            if a[i] != a[-1-i]:
                res = 0
                break
    else:
        res = -1
    return res


if __name__ == "__main__":
    string = 'reviver'
    print(f'Input: {string=}, result: {ispalindrome(string)}')

    string = 'qwerty'
    print(f'Input: {string=}, result: {ispalindrome(string)}')

    string = 'а роза упала на лапу азора'
    mode = 1
    print(f'Input: {string=}, result: {ispalindrome(string)}')
    print(f'Input: {string=} & {mode=}, result: {ispalindrome(string, mode)}')
