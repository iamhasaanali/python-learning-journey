#practice 1
from datetime import datetime, timedelta
today = datetime(2026, 7, 16)
future = datetime(2027, 2, 1)
difference = future - today

print(difference)
print(type(difference))
print(difference.days)
print(difference.seconds)
print(difference.total_seconds())
print("---------------------------------------------------")
#practice 2
from datetime import datetime, timedelta
today = datetime.now()
print("Today:", today.strftime("%d %B %Y"))
in_30_days = today + timedelta(days=30)
print("In 30 Days: ", in_30_days.strftime("%d %B %Y"))
in_2_weeks = today + timedelta(weeks=2)
print("In 2 Weeks: ", in_2_weeks.strftime("%d %B %Y"))
in_5_hours = today + timedelta(hours=5)
print("In 5 Hours", in_5_hours.strftime("%I:%M %p"))
last_week = today - timedelta(days=7)
print("Last week:", last_week.strftime("%d %B %Y"))
last_year = today - timedelta(days=365)
print("Last year:", last_year.strftime("%d %B %Y"))
three_hours_ago = today - timedelta(hours=3)
print("3 hours ago:", three_hours_ago.strftime("%I:%M %p"))
print("---------------------------------------------------")

#practice 3
from datetime import datetime
date1 = datetime (2026, 1, 1)
date2 = datetime(2026, 12, 31)
today = datetime.now()
print(date1 < date2)
print(date1 > today)
print(date1 == date2)

expiry = datetime(2026, 6, 1)
if today > expiry:
    print("Membership Expired!!")
else:
    date_left = (expiry - today).days
    print(f"Membership is valif for {date_left} more days")
print("---------------------------------------------------")
#practice 4
from datetime import datetime
birthday = datetime(1998, 7, 6)
today = datetime.now()
difference = today - birthday
total_days = difference.days
years = total_days // 365
months = (total_days % 365) // 12
days = (total_days % 365) // 30
print(f"You are {years} years {months} months and {days} days old")
print("---------------------------------------------------")
#practice 5
from datetime import datetime
from dateutil.relativedelta import relativedelta
birthday = datetime(1998, 7, 6)
today = datetime.now()
diff = relativedelta(today,birthday)
print(f"you are {diff.years} years {diff.months} months and {diff.days} days old now")
print("---------------------------------------------------")
#practice 6
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def days_until(event_name, event_date):
    today = datetime.now()
    difference = event_date - today
    if difference.days < 0:
        return f"{event_name} has already passed {abs(difference.days)} days ago"
    return f"{difference.days} days until {event_name}!"
def age_calculator(name,birthday):
    today = datetime.now()
    diff = relativedelta(today, birthday)
    return f"{name} is {diff.years} years, {diff.months} months and {diff.days} days old!"

print(days_until("Pakistan Move", datetime(2027, 2, 1)))
print(days_until("New Year 2027", datetime(2027, 1, 1)))
print(days_until("My Birthday 2025", datetime(2025, 7, 6)))
print(age_calculator("Hasaan", datetime(1998, 7, 6)))