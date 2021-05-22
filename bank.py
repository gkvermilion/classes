class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    #def print_protected_data(self):
    #    print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

a = BankAccount('Bob', 50000, 8933939)
a.print_private_data()
# print(a.__name)
# print(a.__balance)
# print(a.__passport)
a.__name = 'hehe'
a.print_private_data()
#use accessify