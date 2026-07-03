from datetime import datetime

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

birthday = datetime(birth_year, birth_month, birth_day)

now = datetime.now()
difference = now - birthday
print(f"You have been alive for {difference.days} days!")