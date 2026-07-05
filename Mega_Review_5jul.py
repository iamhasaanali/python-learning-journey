#Mega Review Challenge 1 of 12

class animal:
    def speak(Self):
        return "I make a sound"
class dog(animal):
    def speak(Self):
        return "Woof!"
    
a1 = animal()
d1 = dog()
print(a1.speak())
print(d1.speak())

#Mega Review Challenge 2 of 12

import pandas as pd
data = {
    "City" : ["sydney", "melbourne", "brisbane", "perth", "adelaide"],
    "population" : [5000000, 4000000, 2500000, 2000000, 1500000]
}
df = pd.DataFrame(data)
print(df.sort_values("population", ascending=False))

#Mega Review Challenge 3 of 12

import pandas as pd
data = {
    "name" : ["Hasaan", "Ali", "Ahmed", "Ayesha", "Fatima"],
    "math_score" : [85, 90, 78, 42, 88],
    "english_score" : [80, 55, 75, 90, 85]
}
df = pd.DataFrame(data)
high_Scorers = df[(df["math_score"] > 60) & (df["english_score"] > 60)]
print(high_Scorers)

#Mega Review Challenge 4 of 12
import random
coins = ["heads", "tails"]
tosses = [random.choice(coins) for i in range(5)]
print(tosses)

#Mega Review Challenge 5 of 12
def bmi_calculator(weight, height):
    bmi = weight / (height * height)
    return round(bmi, 2)
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi< 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

p1 = bmi_calculator(70, 1.75)
print(f"BMI: {p1} — Category: {bmi_category(p1)}")

#Mega Review Challenge 6 of 12
from datetime import datetime
name = input("Enter your name: ")
now = datetime.now()
hour = now.hour
if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
    
print(f"{greeting}, {name}! today is {now.strftime('%A, %d %B %Y')}")

#Mega Review Challenge 7 of 12
while True:
    try:
        num = int(input("Enter a number: "))
        if num > 0 and num < 11:
            print("valid number")
            break
        else:
            print("Invalid input, please enter a valid number.")
    except:
        print("Invalid input, please enter a number.")

#Mega Review Challenge 8 of 12
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [n**2 for n in numbers if n % 3 == 0]
print(result)

#Mega Review Challenge 9 of 12
numbers = [1, 2, 3, 1, 2, 1, 3, 4, 2, 1]
number_count = {}
for n in numbers:
    if n in number_count:
        number_count[n] += 1
    else:
        number_count[n] = 1
print(number_count)

#Mega Review Challenge 10 of 12
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

r1 = rectangle(5, 10)
r2 = rectangle(7, 7)
print(f" Rectangle 1 area: {r1.area()}, perimeter: {r1.perimeter()}, is square: {r1.is_square()}")
print(f" Rectangle 2 area: {r2.area()}, perimeter: {r2.perimeter()}, is square: {r2.is_square()}")

#mega Review Challenge 11 of 12 is in review_notes.py file
#Mega Review Challenge 12 of 12
import pandas as pd
data = {
    "name" : ["Hasaan", "Ali", "Ahmed", "Ayesha", "Fatima"],
    "salary" : [50000, 60000, 45000, 70000, 55000],
    "department" : ["IT", "HR", "Finance", "IT", "HR"]
}
df = pd.DataFrame(data)
high_Salary = df[df["salary"] > 50000]
descending_salary = df.sort_values("salary", ascending=False)
print(f"Employees with salary greater than 50000: {high_Salary}")
print(f"Employees sorted by salary in descending order:
       {descending_salary}")