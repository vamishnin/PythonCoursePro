# 1. Реализовать цикл, формирующий число из вводимых пользователем символов, пока не будет введено слово “stop” (или
# “Stop”, или “STOP”). Если пользователь ввел не числовой символ, вывести предупреждение и запросить новый символ.

def chain_of_numbers():
    chain = ''
    while (user_input := input('Write number ')).lower() != 'stop':
        if user_input.isdigit():
            chain += user_input
        else:
            print('It\'s not a number')
    return chain


print(chain_of_numbers())
