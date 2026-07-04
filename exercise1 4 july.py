from datetime import datetime

now = datetime.now()
future = datetime(2027, 1, 1)
difference = future - now
weeks = difference.days // 7
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60

print("new year starts in:", difference.days, "days", hours, "hours", minutes, "minutes")