class BankAccount:
    total_BankAccounts = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_BankAccounts += 1
    def deposit(self):
        amount = int(input("Enter amount: "))
        self.balance = self.balance + amount
        print(self.owner, "your current balance is: ", self.balance)
    def withdrawl(self):
        minus = int(input("Enter amount: "))
        self.balance = self.balance - minus
        print(self.owner, "your current balance is", self.balance)

b1 = BankAccount("Hasaan", 5000)
b2 = BankAccount("Ali", 9877)

b1.deposit()
print(b1.balance)
b1.withdrawl()
print("Total Bank Accounts", BankAccount.total_BankAccounts)