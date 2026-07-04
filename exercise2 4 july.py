from datetime import datetime

name = input("Enter your name: ")
day = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year: "))
birthday = datetime(year, month, day)

print(f"\nHello, {name}!")
print("Birthday Format 1:", birthday.strftime("%d/%m/%Y"))
print("Birthday Format 2:", birthday.strftime("%B %d, %Y"))
print("Birthday Format 3:", birthday.strftime("%A, %d %B %Y"))

today = datetime.now()
next_birthday = datetime(today.year, month, day)

days_until = (next_birthday - today).days

print(f"Days until your next birthday: {days_until}")

print("You were born on a", birthday.strftime("%A"))
