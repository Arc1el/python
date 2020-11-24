class Bank:
    def __init__(self):
        self.__balance = 1000000
        print("처음 잔액 : ", "{:,}".format(self.__balance), "\n")

    def withdraw(self, money):
        self.__balance -= money
        print("통장에 ",  "{:,}".format(money), "원 출금되었음")
        return self.__balance

    def deposit(self, money):
        self.__balance += money
        print("통장에 ",  "{:,}".format(money), "원 입금되었음")
        return self.__balance

account = Bank()
print("현재잔액 : ", "{:,}".format(account.deposit(100000)), "원\n")
print("현재잔액 : ", "{:,}".format(account.withdraw(10000)), "원\n")
