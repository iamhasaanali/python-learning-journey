name = input("What is your name? ").title()
number = input("What is your phone number? ")
with open("/Users/hasaanali/Documents/contacts.txt", "a")as file:
    file.write(name + "\n")
    file.write(number + "\n")


with open("/Users/hasaanali/Documents/contacts.txt", "r")as file:
    content = file.read()
    print("--- Your Contacts ---")
    print(content)