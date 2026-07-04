
  #Exercise 1: Random Number and Choice
import random
number = random.randint(1, 100)
print(number)
 
hobbies = ["cricket", "football", "tennis", "basketball"]
choice = random.choice(hobbies)
print(choice)

   #Exercise 2: Math Functions

import math
print(math.sqrt(144))
print(round(math.pi, 4))
print(math.ceil(7.5))
print(math.floor(7.5))

   #Exercise 3: Date and Time

from datetime import datetime
now = datetime.now()
future_date = datetime(2026, 12, 25)
time_difference = future_date - now
print("Time until Christmas 2026:", time_difference.days, "days")
print(now.strftime("Today is %A, %d %B %Y"))

   #Exercise 4: Calculator Tools
import calculator_tools 
n1 = calculator_tools.square(5)
n2 = calculator_tools.is_even(10)
n3 = calculator_tools.percentage(25, 200)
print("Square of 5:", n1)
print("Is 10 even?:", n2)
print("Percentage of 25 out of 200:", n3)

   #Exercise 5: Combine f-strings + datetime + a function:

from datetime import datetime
def time_greeting(name):
    now = datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return f"{greeting}, {name}! The current time is {now.strftime('%H:%M:%S')}"

name = time_greeting("Hasaan")
print(name)