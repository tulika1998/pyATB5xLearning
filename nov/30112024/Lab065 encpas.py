class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance #public
        self.__account_number = account_number #private
    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_the_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("not allowed")

icici = Bank(9484778393, 200)
icici.deposit(200)
icici.check_balance()
icici.show_me_the_account_number(True)
icici.show_me_the_account_number(False)


