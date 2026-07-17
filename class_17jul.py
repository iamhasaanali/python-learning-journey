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
people.sort(key=lambda x: x["age"], reverse=True)
print("\nPeople sorted oldest to youngest")
for person in people:
    print(f"{person["name"]}: {person["age"]} years old")

print("---------------------------------------------------")
#exercise 2
from datetime import datetime, timedelta

today = datetime.now()

topics = [
    "Python review",
    "Pandas practice", 
    "datetime deep dive",
    "OOP review",
    "zip() practice",
    "groupby() practice",
    "Mini project"
]
for i in range(7):
        day = today + timedelta(days=i)
        topic = topics[i]
        day_name = day.strftime("%A")
        print(f"Day {i + 1} - {day.strftime('%A %d %B %Y')}: {topic}")
        if day_name == "Saturday" or day_name == "Sunday":
             print(f"⚠️ Warning: {day_name} {day.strftime('%d %B')} is a weekend — rest day!")
print("---------------------------------------------------")
#exercise 3
from datetime import datetime
class Deadline:
    def __init__(self, task_name, due_date):
         self.task_name = task_name
         self.due_date = due_date
        
    def days_remaining(self):
         today = datetime.now()
         difference = self.due_date - today
         return difference.days
    def status(self):
         days = self.days_remaining()
         if days < 0:
              return "OVERDUE"
         elif days == 0:
              return "DUE TODAY"
         elif days <= 3:
              return "URGENT"
         else:
              return "ON TRACK"
d1 = Deadline("Python Assignment", datetime(2026, 7, 18))
d2 = Deadline("Pandas Project", datetime(2026, 7, 20))
d3 = Deadline("SQL Homework", datetime(2026, 8, 1))
d4 = Deadline("ML Report", datetime(2026, 6, 1))

deadlines = [d1, d2, d3, d4]

for deadline in deadlines:
    days = deadline.days_remaining()
    status = deadline.status()
    print(f"{deadline.task_name}: {status} — {days} days remaining")