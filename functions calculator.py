def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

number1 = int(input("enter first number "))
number2 = int(input("enter second number "))

print("Added", add(number1, number2))
print("Subtracted", subtract(number1, number2))
print("Multiplied", multiply(number1, number2))
print("Divided", divide(number1, number2))
