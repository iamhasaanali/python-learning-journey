expense_name = input("Enter expense name: ")
amount = input("Enter amount: $")

with open("/Users/hasaanali/Documents/expenses.txt", "a") as file:
    file.write(expense_name + " - $" + amount + "\n")








with open("/Users/hasaanali/Documents/expenses.txt", "r") as file:
    content = file.read()
    print("--- All Expenses ---")
    print(content)