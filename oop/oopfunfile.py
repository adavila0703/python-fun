class BankProfile:

    def __init__(self, accountname, in_deposit):
        self.accountname = accountname
        self.balance = in_deposit

    def __str__(self):
        return print(f"{self.accountname}'s account.")

    def __len__(self):
        return print(f"Balance is {self.balance}")

    def widthdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

