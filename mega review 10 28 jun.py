while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 / num2
            print(result)
            break
    except:
        print("Please enter a valid number")