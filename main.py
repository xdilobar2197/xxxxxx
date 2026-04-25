# xxxxxx

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Yetarli mablag‘ yo‘q")

    def show_balance(self):
        print(f"{self.owner} balans: {self.balance}$")


# Test
account = BankAccount("Ali", 1000)

account.deposit(500)
account.show_balance()      # Ali balans: 1500$

account.withdraw(2000)      # Yetarli mablag‘ yo‘q
account.withdraw(300)

account.show_balance()      # Ali balans: 1200$
