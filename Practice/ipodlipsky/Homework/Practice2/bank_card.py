import datetime

'''Необходимо создать алгоритм работы банковского счета. 
Мы можем пополнять баланс за счет входящих платежей или списания сретств с баланса.
Мы можем смотреть текущий баланс и после каждой операции зачисления или списания в историю записывается 
тип операции, текущий баланс и время платежа.'''

class Accout():
# history -  пустой список, в который будет добавляться информация о транзакции:
# тип операции - снятие или зачисление, баланс b время операции

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def curent_time():
        dt = datetime.datetime.now()
        return dt
        #pytz.utc.localize(datetime.utcnow())

# метод, позволяет пополнить баланс
    def deposit(self, amount):
        print(f'You put {amount} units')
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self.curent_time()])

# метод, позволяет снять деньги с счета
    def credit(self, amount):

        if self.__balance > amount:
            print(f'You spent {amount} units')
            self.__balance -= amount
            self.show_balance()
            self._history.append([-amount, self.curent_time()])
        else:
            print('The requested amount is more than your balance ')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

# история состоит из списка из двух элементов. в методе show_history мы распаковываем эти элементы
    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                print(f'{amount} {transaction} on {self.curent_time()} ')
            else:
                transaction = 'credited'
                print(f'{amount} {transaction} on {self.curent_time()} ')

a = Accout('Igor', 0)

a.deposit(100)
a.deposit(100)
a.deposit(100)
a.credit(30)
a.show_history()
