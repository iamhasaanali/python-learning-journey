while True:
    password = input("Please enter your password: ")
    key = ("python123")
    if password != key:
        print("wrong password!")
    else:
        print("Access granted!")
        break