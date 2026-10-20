class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, balance):
        self.__balance += balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        else:
            print("Insufficient funds for withdrawal.")


bank = Bank("Suraj", 90)

bank.withdraw(100)