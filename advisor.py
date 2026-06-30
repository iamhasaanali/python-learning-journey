name = input ("what is your name? ")
age = int(input("how old are you? "))
money = int(input("how much money do you have in savings? "))
if age >= 60:
        print("hey" , name , "you should be retiring soon!")
elif age >= 30:
        print("hey" , name , "you should look into investing more for you future!")
elif age >= 18:
        print("hey" , name , "you should enjoy your life a little bit more!")
else:
        print("hey" , name , "you should focus on school")
if money >= 10000:
        print("your savings are great!")
elif money >= 1000:
        print("you saving are okaysih!")
else:
        print("you need to focus on savings" , name , "!")