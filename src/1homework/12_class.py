класс BankAccount (объект):
    def __init __ (self, initial_balance = 0):
        self.balance = начальный_баланс
    депозит (сам, сумма):
        self.balance + = сумма
    def вывести (самостоятельно, сумма):
        self.balance - = количество
    def overdrawn (self):
        возврат self.balance <0
my_account = BankAccount (15)
my_account.withdraw (50)
print (my_account.balance, my_account.overdrawn ())