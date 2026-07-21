#exercise 1
people = [
    {"name": "Hasaan", "age": 28},
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 30},
    {"name": "Ahmed", "age": 25},
]
people.sort(key=lambda x: x["age"])
for person in people:
    print(f"{person["name"]}: {person["age"]} years old")
print("\nPeople sorted oldest to youngest")
people.sort(key=lambda x: x["age"], reverse=True)
for person in people:
    print(f"{person["name"]}: {person["age"]} years old")
print("--------")
youngest = min(people, key=lambda x: x["age"])
print(f"Youngest person is {youngest["name"]} and he/she is {youngest["age"]} years old")
print("--------")
oldest = max(people, key=lambda x: x["age"])
print(f"Oldest person is {oldest["name"]} and he/she is {oldest["age"]} years old")
print("\n -------------------------------")
#exercise 2
from datetime import datetime 
from dateutil.relativedelta import relativedelta
today = datetime.now()

people = [
    {"name": "Hasaan", "birthday": datetime(1998, 7, 6)},
    {"name": "Ali", "birthday": datetime(2001, 3, 15)},
    {"name": "Sara", "birthday": datetime(1995, 11, 22)},
    {"name": "Ahmed", "birthday": datetime(2000, 8, 10)},
]
for person in people:
    diff = relativedelta(today,person["birthday"])
    person["age"] = diff.years
    print(f"{person["name"]} is {person["age"]} years old")

oldest = max(people, key=lambda x: x["age"])
youngest = min(people, key=lambda x: x["age"])
print(f"olest is {oldest["name"]} : {oldest["age"]}")
print(f"Youngest us {youngest["name"]} : {youngest["age"]}")
print("\n -------------------------------")

#exercise 3

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

people = [
    {"name": "Hasaan", "birthday": datetime(1998, 7, 6)},
    {"name": "Ali", "birthday": datetime(2001, 3, 15)},
    {"name": "Sara", "birthday": datetime(1995, 11, 22)},
    {"name": "Ahmed", "birthday": datetime(2000, 8, 10)},
]
for person in people:
    diff = relativedelta(today,person["birthday"])
    person["age"] = diff.years
    next_bday = datetime(today.year, person["birthday"].month, person["birthday"].day)
    if next_bday < today:
        next_bday = datetime(today.year +1, person["birthday"].month, person["birthday"].day)
    days_until =(next_bday - today).days
    person["days_until_bday"] = days_until
    print(f"{person["name"]} next birthday is in {days_until} days")

closest = min(people, key=lambda x: x["days_until_bday"])
print(f"{closest["name"]} has birthday in {closest["days_until_bday"]} days")
print("\n -------------------------------")

#exercise 4

scores = [
    ("Hasaan", 85, "Math"),
    ("Ali", 92, "Science"),
    ("Sara", 78, "Math"),
    ("Ahmed", 95, "Science"),
    ("Fatima", 88, "Math"),
]
for score in scores:
    print(f"{score[0]} scored {score[1]} in {score[2]}")
print("-------")
scores.sort(key=lambda x: x[1], reverse=True)
for score in scores:
    print(f"{score[0]} scored {score[1]} in {score[2]}")
highest = max(scores, key=lambda x: x[1])
lowest = min(scores, key=lambda x: x[1])
print(f"{highest[0]} has scored highest with {highest[1]} numbers")
print(f"{lowest[0]} has scored lowest with {lowest[1]} numbers")

print("\n -------------------------------")

#exercise 5
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

movies = [
    {"title": "Inception", "release": datetime(2010, 7, 16), "rating": 8.8},
    {"title": "Interstellar", "release": datetime(2014, 11, 7), "rating": 8.6},
    {"title": "The Dark Knight", "release": datetime(2008, 7, 18), "rating": 9.0},
    {"title": "Oppenheimer", "release": datetime(2023, 7, 21), "rating": 8.3},
]
for movie in movies:
    diff = relativedelta(today,movie["release"])
    movie["age"] = diff.years
    print(f"{movie["title"]} is {movie["age"]} old movie with rating of {movie["rating"]}")
print("------")
oldest = max(movies, key=lambda x: x["age"])
highest = max(movies, key=lambda x: x["rating"])
print(f"{oldest["title"]} is oldest movie in this list")
print("-------")
print(f"{highest["title"]} is highest rated movie with ratings of {highest["rating"]} in this list")
print("------")
movies.sort(key=lambda x: x["rating"], reverse=True)
for movie in movies:
    print(f"{movie["title"]} has ratings if {movie["rating"]}")

print("\n -------------------------------")

#exercise 6
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

today = datetime.now()

employees = [
    {"name": "Hasaan", "department": "IT", "salary": 70000, "joined": datetime(2020, 3, 15)},
    {"name": "Ali", "department": "HR", "salary": 45000, "joined": datetime(2022, 7, 1)},
    {"name": "Sara", "department": "IT", "salary": 65000, "joined": datetime(2019, 11, 20)},
    {"name": "Ahmed", "department": "Finance", "salary": 80000, "joined": datetime(2018, 5, 10)},
    {"name": "Fatima", "department": "HR", "salary": 55000, "joined": datetime(2021, 9, 5)},
]

for emp in employees:
    diff = relativedelta(today,emp["joined"])
    emp["years_worked"] = diff.years
    print(f"{emp["name"]} is working in {emp["department"]} department for {diff.years} years")
it_employees =[emp for emp in employees if emp["department"] == "IT"]
print("\nIT Department employees:")
for emp in it_employees:
    print(f"  {emp['name']} — ${emp['salary']} — {emp['years_worked']} years")
highest = max(employees, key=lambda x: x["salary"])
print(f"{highest["name"]} has highest salary")
employees.sort(key=lambda x: x["salary"], reverse=True)
for emp in employees:
    print(f"{emp["name"]} : {emp["salary"]}")

print("\n -------------------------------")

#exercise 7
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
employees = [
    {"name": "Hasaan", "department": "IT", "salary": 70000, "joined": datetime(2020, 3, 15)},
    {"name": "Ali", "department": "HR", "salary": 45000, "joined": datetime(2022, 7, 1)},
    {"name": "Sara", "department": "IT", "salary": 65000, "joined": datetime(2019, 11, 20)},
    {"name": "Ahmed", "department": "Finance", "salary": 80000, "joined": datetime(2018, 5, 10)},
    {"name": "Fatima", "department": "HR", "salary": 55000, "joined": datetime(2021, 9, 5)},
]
for e in employees:
    diff = relativedelta(today, e["joined"])
    e["years_worked"] = diff.years
    print(f"{e["name"]} has been working here for {diff.years}")
print("-------")
df = pd.DataFrame(employees)
print(df.shape)
print("-------")
print(df.describe())
print("-------")
it_employees =[e for e in employees if e["department"] == "IT"]
for e in it_employees:
    print(f"{e["name"]} : {e["department"]} : {e["salary"]}")
print("-------")
print(df.groupby("department")["salary"].mean())
print("-------")
print(df.sort_values("salary", ascending=False))
print("-------")

df.to_csv("/Users/hasaanali/Documents/My_Learning/class_18jul.csv", index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/class_18jul.csv")
print(new_df)
print("\n -------------------------------")

#exercise 8
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
students = [
    {"name": "Hasaan", "birthday": datetime(1998, 7, 6), "subject": "Math", "score": 85},
    {"name": "Ali", "birthday": datetime(2001, 3, 15), "subject": "Science", "score": 42},
    {"name": "Sara", "birthday": datetime(1995, 11, 22), "subject": "Math", "score": 92},
    {"name": "Ahmed", "birthday": datetime(2000, 8, 10), "subject": "Science", "score": 78},
    {"name": "Fatima", "birthday": datetime(1990, 5, 3), "subject": "Math", "score": 55},
]
for s in students:
    diff = relativedelta(today,s["birthday"])
    s["age"] = diff.years
    if s["score"] >= 90:
        grade = "A"
    elif s["score"] >= 75:
        grade = "B"
    elif s["score"] >= 50:
        grade = "C"
    else:
         grade = "F"
    s["grade"] = grade
    print(f"{s["name"]} : {s["grade"]}")
print("-------")
oldest = max(students, key=lambda x: x["age"])
print(f"{oldest["name"]} is oldest in class")
print("-------")
highest = max(students, key=lambda x: x["score"])
print(f"{highest["name"]} has highest scoeres in class")
print("-------")
passed = [s for s in students if s["score"] >= 50]
for s in passed:
    print(f"{s["name"]} : {s["score"]} passed")
print("-------")
df = pd.DataFrame(students)
print(df.groupby("subject")["score"].mean())
print("-------")
df.to_csv("/Users/hasaanali/Documents/My_Learning/class_21july.csv" , index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/class_21july.csv")
print(new_df)