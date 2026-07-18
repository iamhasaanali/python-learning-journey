from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

today = datetime.now()

friends = [
    {"name": "Ali", "birthday": datetime(1999, 8, 15)},
    {"name": "Sara", "birthday": datetime(2001, 7, 25)},
    {"name": "Ahmed", "birthday": datetime(1998, 9, 3)},
    {"name": "Fatima", "birthday": datetime(2000, 7, 20)},
]
for friend in friends:
    diff = relativedelta(today,friend["birthday"])
    friend["age"] = diff.years
    print(f"{friend["name"]} is {friend["age"]} years old")
    next_bday = datetime(today.year,friend["birthday"].month,friend["birthday"].day)
    if next_bday < today:
        next_bday = datetime(today.year + 1,friend["birthday"].month,friend["birthday"].day)
    days_until = (next_bday - today).days
    friend["days_until_bday"] =  days_until
    print(f"{friend["name"]} next birthday is in {days_until} days")

closest = min(friends, key=lambda x: x["days_until_bday"])
print(f"{closest["name"]} has birthday in {closest["days_until_bday"]} days")









