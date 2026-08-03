print("\n------exercise 1------")
#exercise 1
import pandas as pd

students = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "course_id": [1, 2, 1, 4, 2],
    "score": [85, 92, 78, 95, 88]
})

courses = pd.DataFrame({
    "course_id": [1, 2, 3],
    "course_name": ["Python", "Data Science", "ML"],
    "instructor": ["Mr. Khan", "Ms. Smith", "Mr. Ali"]
})
print(pd.merge(students,courses, on="course_id", how="inner"))
print("-------------------------------")
print(pd.merge(students,courses, on="course_id", how="left"))

print("\n------exercise 2------")
#exercise 2
merge = pd.merge(students,courses, on="course_id", how="inner")
print(merge.pivot_table(values="score", index="course_name", aggfunc="mean", fill_value=0))
print("-------------------------------")
print(merge.pivot_table(values="score", index="course_name", aggfunc="max"))

print("\n------exercise 3------")
#exercise 3
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000]
}


df = pd.DataFrame(data)
print(df.groupby("department")["salary"].agg(["mean","max","min"]).reset_index())
print("-------------------------------")
df["dept_avg"] = df.groupby("department")["salary"].transform("mean")
df["above_avg"] = df["salary"] > df["dept_avg"]
print(df)

print("\n------exercise 4------")
#exercise 4
import pandas as pd

data = {
    "product": ["iPhone 17 Pro", "samsung galaxy", "MacBook Air", "IPAD MINI", "surface pro"],
    "brand": ["Apple", "samsung", "Apple", "APPLE", "Microsoft"],
    "price": [2500, 1200, 1800, 900, 1500]
}

df = pd.DataFrame(data)
df["product"] = df["product"].str.title()
df["brand"] = df["brand"].str.title()
print(df)
print("-------------------------------")
print(df[df["product"].str.contains("pro", case=False)])
print("-------------------------------")
print(df[df["price"] > 1500])
print("-------------------------------")
df["discount"] = df["price"] * 0.85
print(df)

print("\n------exercise 5------")
#exercise 5
import pandas as pd
cities = ["Sydney", "Karachi", "London", "Dubai", "Melbourne"]
countries = ["Australia", "Pakistan", "England", "UAE", "Australia"]
populations = [5000000, 15000000, 9000000, 3000000, 5000000]
avg_temps = [22, 28, 12, 35, 18]
if len(cities)== len(countries) == len(populations) == len(avg_temps):
    combine = [
        {"city" : city, "country" : country, "population": population, "avg_temp": avg_temp} 
        for city,country,population,avg_temp in zip(cities,countries,populations,avg_temps)
    ]
else:
    ("lengths doesnt match")

df = pd.DataFrame(combine)
print(df)
print("-------------------------------")
print(df[df["avg_temp"] > 25])
print("-------------------------------")
print(df.sort_values("population", ascending=False))

print("\n------exercise 6------")
#exercise 6
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

events = [
    {"name": "Pakistan Move", "date": datetime(2027, 2, 1)},
    {"name": "Eid 2027", "date": datetime(2027, 3, 30)},
    {"name": "My Birthday", "date": datetime(2026, 7, 6)},
    {"name": "New Year 2027", "date": datetime(2027, 1, 1)},
]
for e in events:
    diff = e["date"] - today
    e["days"] = diff.days
    if e["days"] > 0 :
        print(f"{e['name']}: {e["days"]} days away!")
    elif e["days"] < 0 :
        print(f"{e['name']}: {abs(e["days"])} days ago!")
    else:
        print(f"Today is {e["name"]}! ")

future_events = [e for e in events if e["days"] > 0]
closest = min(future_events, key=lambda x: x["days"])
farthest = max(future_events, key=lambda x: x["days"])
print(f"{closest["name"]} is the upcoming event!")
print(f"{farthest["name"]} is last")

print("\n------exercise 7------")
#exercise 7
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Subscription:
    def __init__(self,customer,plan,monthly_price,start_date):
        self.customer = customer
        self.plan = plan
        self.monthly_price = monthly_price
        self.start_date = start_date
    def months_active (self):
        today = datetime.now()
        diff = relativedelta(today,self.start_date)
        months = diff.years * 12 + diff.months
        return months
    def total_paid(self):
        return self.months_active() * self.monthly_price
    def is_premium(self):
        if self.monthly_price > 50:
            return True
        else:
            return False

s1 = Subscription("Hasaan", "Pro", 100, datetime(2024, 1, 1))
s2 = Subscription("Ali", "Basic", 30, datetime(2025, 6, 1))
s3 = Subscription("Sara", "Pro", 100, datetime(2023, 3, 1))
s4 = Subscription("Ahmed", "Basic", 30, datetime(2026, 1, 1))
Subscriptions = [s1,s2,s3,s4]
data = []
for s in Subscriptions:
    data.append({
        "cutomer": s.customer,
        "plan" : s.plan,
        "premium" : s.is_premium(),
        "month_active" : s.months_active(),
        "total_paid": s.total_paid()
    })

df= pd.DataFrame(data)
print(df)
print("-------------------------------")
premium_mmb = df[df["premium"]==True]
print(premium_mmb)
print("-------------------------------")
print(df.sort_values("total_paid", ascending=False))

print("\n------exercise 8------")
#exercise 8
import pandas as pd

df = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "experience": [6, 2, 8, 4, 1],
    "salary": [70000, 35000, 85000, 55000, 28000],
    "certifications": [3, 1, 5, 2, 0]
})
def employee_rank(row):
    if row["experience"] > 5 and row["certifications"] > 2:
        return f"Expert"
    elif row["experience"] >3 and row["certifications"] > 1:
        return "Intermediate"
    else:
        return f"Beginner"

df["rank"] = df.apply(employee_rank, axis=1)
print(df)
print("-------------------------------")
print(df[df["rank"]=="Expert"])
print("-------------------------------")
print(df.sort_values("salary", ascending=False).head(1))

print("\n------exercise 9------")
#exercise 9
scores = [92, 78, 85, 95, 68, 88, 72, 91, 65, 83]
print(scores[:3])
print("-------------------------------")
print(scores[-3:])
print("-------------------------------")
print(scores[::2])
print("-------------------------------")
print(scores[::-1])
print("-------------------------------")
print(scores[3:7])
scores.sort(reverse=True)
print(scores[:3])


print("\n------exercise 10------")
#exercise 10
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "birth_year": [1998, 2001, 1995, 2000, 1990],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)
def age_years(birth_year):
    today = datetime.now()
    birthday = datetime(birth_year, 1, 1)
    diff = relativedelta(today, birthday)
    return diff.years
df["age"] = df["birth_year"].apply(age_years)
print(df)
print("-------------------------------")
def salary_band(row):
    if row["salary"] > 70000:
        return "High"
    elif row["salary"] > 50000:
        return "Medium"
    else:
        return "Low"
df["band"] = df.apply(salary_band, axis=1)
print(df.groupby("department")["salary"].mean())
print("-------------------------------")
print(df[df["band"] == "High"])

print("\n------exercise 11------")
#exercise 11 is in mega_review_03aug.py

print("\n------exercise 12------")
#exercise 12
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

employees = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "dept_id": [1, 2, 1, 3, 2],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "hire_date": [
        datetime(2019, 3, 15),
        datetime(2022, 7, 1),
        datetime(2018, 11, 20),
        datetime(2021, 5, 10),
        datetime(2017, 9, 5)
    ]
})

departments = pd.DataFrame({
    "dept_id": [1, 2],
    "dept_name": ["IT", "HR"],
    "location": ["Sydney", "Karachi"]
})
merged = pd.merge(employees,departments, on="dept_id", how="left")
def years_worked(row):
    today = datetime.now()
    diff = relativedelta(today,row["hire_date"])
    if diff.years > 5:
        return "Senior"
    elif diff.years > 3:
        return "Mid"
    else:
        return "Junior"
merged["level"] = merged.apply(years_worked, axis=1)
merged["dept_avg"] = merged.groupby("dept_name")["salary"].transform("mean")
merged["above_avg"] = merged["salary"] > merged["dept_avg"]
print(merged)
print("-------------------------------")
print(merged[merged["level"] == "Senior"])
print("-------------------------------")
print(merged.groupby("dept_name")["salary"].agg(["mean","max"]))

