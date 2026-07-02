from datetime import datetime

now = datetime.now()
future = datetime(2027, 2, 1)
difference = future - now
weeks = difference.days // 7
days_remaining = difference.days % 7

print("year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

print("---------------------------------")

print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%I:%M %p"))

print("---------------------------------")

print("Days until Pakistan: ",difference.days)

print("---------------------------------")

print(f"Time untill Pakistan move:")
print(f"Total days: {difference.days}")
print(f"That's {weeks} weeks and {days_remaining} days")
print(f"Keep coding everyday Hasaan!")
