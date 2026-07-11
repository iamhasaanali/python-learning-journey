#exercise 1
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", None, "Fatima"],
    "age": [27, None, 25, 30, None],
    "score": [85, 92, None, 78, 88]
}
df = pd.DataFrame(data)
print(df.isnull().sum())
print("-----")
df["age"]= df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())
print(df)
print("-----")
df = df.dropna(subset=["name"])
print(df)

print("-------------------------------------------------")

#exercie 2
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "salary": [70000, 45000, 65000, 80000, 50000, 75000]
}
df = pd.DataFrame(data)
print(df.describe())
print("-----")
print(df.groupby("department")["salary"].mean())
print("-----")
print(df.sort_values("salary", ascending=False).head(1))
print("-----")
df["senior_pay"] = df["salary"] > 65000
print(df)

print("-------------------------------------------------")

#exercise 3
import pandas as pd

df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/students.csv")
print(df.value_counts("city"))
print("-----")
print(df.groupby("city")["grade"].mean())
print("-----")
london = df[df["city"] == "London"]
print(london)
print("-----")
print(df.sort_values("grade", ascending=False).head(2))

print("-------------------------------------------------")

#exercise 4
import pandas as pd
data = {
    "name": ["Babar", "Kohli", "Smith", "Root", "Williamson"],
    "runs": [85, 120, 45, 95, 67],
    "wickets": [0, 0, 2, 1, 0],
    "country": ["Pakistan", "India", "Australia", "England", "New Zealand"]
}
df = pd.DataFrame(data)
print(df.shape)
print("-----")
print(df.columns)
print("-----")
print(df.head(3))
print("-----")
print(df.describe())
high_score = df[df["runs"] > 50]
print(high_score)
print("-----")
print(df.sort_values("runs", ascending=False))

print("-------------------------------------------------")

#exercise 5
import pandas as pd
data = {
    "city": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
    "temperature": [22, 18, 28, 25, 20],
    "humidity": [65, 70, 80, 55, 60],
    "rainfall": [120, 150, 90, 80, 110]
}
df = pd.DataFrame(data)
print(df.describe())
print("-----")
print(df.sort_values("temperature", ascending=False).head(1))
print("-----")
humid = df[(df["humidity"] > 60) & (df["rainfall"] > 100)]
print(humid)
print("-----")
df["hot_city"] = df["temperature"] > 22
print(df)

print("-------------------------------------------------")

#exercise 6
import pandas as pd
data = {
    "student": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima", "Omar", "Zara"],
    "math": [85, 92, 78, 95, 60, 88, 72],
    "english": [80, 55, 90, 85, 75, 92, 68],
    "science": [90, 88, 72, 78, 85, 76, 95]
}
df = pd.DataFrame(data)
df["average"] = df[["math", "english", "science"]].mean(axis=1)
print(df.sort_values("average", ascending=False).head(3))
passed= df[df[["math", "english", "science"]].min(axis=1) > 75]
print("-----")
print(passed)
print("-----")
print(len(passed))
print("-------------------------------------------------")


#exercise 7
subjects = ["Math", "English", "Science", "History", "Art"]
teachers = ["Mr. Khan", "Ms. Smith", "Mr. Ali", "Ms. Jones", "Mr. Brown"]
students = [30, 25, 28, 22, 18]
faculty = dict(zip(subjects, teachers))
for subject,teacher in faculty.items():
    print(f"{teacher} teaches {subject}")

print("-----")

for subjects,teachers,students in zip(subjects,teachers,students):
    print(f"{subjects} is taught by {teachers} with {students} students in class")

print("-------------------------------------------------")

#exercise 8
classroom = [
    ["Hasaan", "Ali", "Sara"],
    ["Ahmed", "Fatima", "Omar"],
    ["Zara", "James", "Maria"]
]
for row in classroom:
      for item in row:
        print(item, end=" ")
      print()
print("-----")
print(classroom[1])
print("-----")
print(classroom[0][-1])
print("-----")
total = 0
for row in classroom:
    total += len(row)

print("total student: ", total)

print("-------------------------------------------------")

#exercise 9
from datetime import datetime
now = datetime.now()
future = datetime(2027, 6, 17)
eid = future - now
weeks = eid.days // 7
days_remaining = eid.days % 7
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%I:%M %p"))
print("-----")
print(eid.days)
print(f"{eid.days} days, {weeks} weeks and {days_remaining} days until EID!")
print("-------------------------------------------------")

#exercise 10
import random
numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
item = ["Hasaan", "Ali", "Sara", "Ahmed"]
choice = random.choice(item)
print(choice)

from math import sqrt
print(sqrt(225))
import math
pi = round(math.pi, 3)
print(pi)
print(math.ceil(9.4))
print(math.floor(9.4))
print("-------------------------------------------------")

#exercise 11
import pandas as pd
data = {
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [70000, 45000, 65000, 80000, 55000],
    "age": [27, 32, 25, 35, 29]
}
df = pd.DataFrame(data)
df["experienced"] = df["age"] > 28
print(df.groupby("department")["salary"].mean())
filtered = df[(df["experienced"]) & (df["salary"] > 60000)]
print(filtered)
filtered.to_csv("/Users/hasaanali/Documents/My_Learning/mega_review_12jul.csv", index=False)

new_df = pd.read_csv("/Users/hasaanali/Documents/My_Learning/mega_review_12jul.csv")
print(new_df)

#exercise 12
from datetime import datetime
today = datetime.now().strftime("%d %B %Y")
name = input("What is expense name? ").title()
amount = input("how much is it? ")
with open("/Users/hasaanali/Documents/My_Learning/expenses_review.txt", "a")as file:
    file.write(f"{today} — i spent ${amount} on {name}\n")

with open("/Users/hasaanali/Documents/My_Learning/expenses_review.txt", "r")as file:
    content = file.read()
    print("--- expenses ---")
    print(content)

print("-------------------------------------------------")