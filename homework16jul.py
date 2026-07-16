from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
today = datetime.now()
events = [
    {"name": "Pakistan Move", "date": datetime(2027, 2, 1)},
    {"name": "New Year 2027", "date": datetime(2027, 1, 1)},
    {"name": "My Birthday", "date": datetime(2026, 7, 6)},
    {"name": "Christmas 2026", "date": datetime(2026, 12, 25)},
    {"name": "Eid 2027", "date": datetime(2027, 6, 17)},
]
for event in events:

    name = event["name"]
    date = event["date"]
    difference = date - today
    days = difference.days
    
    if days > 0:
        print(f"{name}: {days} days away")
    elif days < 0:
        print(f"{name}: already passed {abs(days)} days ago!")
    else:
        print(f"Today is {name}!")
print("---------------------------------------------------")
future_events = [(event["name"], (event["date"] - today).days)
                 for event in events 
                 if (event["date"] - today).days > 0]
future_events.sort(key=lambda x: x[1])
print(future_events)
print(f"Closest : {future_events[0][0]} ({future_events[0][1]} days)")
print(f"Furthest : {future_events[-1][0]} ({future_events[-1][1]} days)")

def is_this_month(event_date):
    return event_date.month == today.month and event_date.year == today.year

print("\nEvents this month:")
for event in events:
    if is_this_month(event["date"]):
        print(f"→ {event['name']} on {event['date'].strftime('%d %B %Y')}")

#exercise 2
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
    diff = relativedelta(today, person["birthday"])
    person["age"] = diff.years
    print(f"{person['name']} is {diff.years} years, {diff.months} months and {diff.days} days old!")
print(people[0])