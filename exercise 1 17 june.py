while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Added: ", num1 + num2 )
        print("Subtracted:", num1 - num2)
        print("Multiplied:", num1 * num2)
        print("Divided:", round(num1 / num2 , 2))
        break
    except:
        print("Invalid entry")
    
   


