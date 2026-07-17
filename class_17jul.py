from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
people = [
    {"name": "Hasaan", "birthday": datetime(1998, 7, 6)},
    {"name": "Ali", "birthday": datetime(2001, 3, 15)},
    {"name": "Sara", "birthday": datetime(1995, 11, 22)},
    {"name": "Ahmed", "birthday": datetime(2000, 8, 10)},
    {"name": "Fatima", "birthday": datetime(1990, 5, 3)},
]
for person in people:
    diff = relativedelta(today,person["birthday"])
    person["age"] = diff.years
    print(f"{person["name"]} is {diff.years} years old!")

print("---------------------------------------------------")

oldest = max(people, key=lambda x:x["age"])
youngest = min(people, key=lambda x:x["age"])
print(f"{oldest["name"]} is oldest he/she is {oldest["age"]} years old")
print(f"{youngest["name"]} is youngest and he/she is {youngest["age"]} years old")

total_age = 0
for person in people:
    total_age += person["age"]
average_age = total_age / len(people)
print(f"Average age is {average_age:.1f} years")
print("---------------------------------------------------")
people.sort(key=lambda x:x["age"], reverse=True)
print("\nPeople sorted oldest to youngest")
for person in people:
    print(f"{person["name"]}: {person["age"]} years old")