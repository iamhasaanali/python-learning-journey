password= ""
while len(password) <=6:
    password=input("enter the password: ")
    if len(password) <6:
        print("too weak try again!")
    else:
        print("Strong password!")

